import sqlite3
import bcrypt
import os
import sys

# Ensure we can import from the current directory
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from hiring_platform.config import Config

def register_user(email, password, role, company_id=None):
    db_path = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'hiring_platform', 'database.sqlite')
    # If not found there, try the config path
    if not os.path.exists(db_path):
        db_path = Config.DATABASE

    try:
        conn = sqlite3.connect(db_path)
        cursor = conn.cursor()
        
        hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt()).decode('utf-8')
        
        cursor.execute(
            "INSERT INTO users (email, password_hash, role, company_id) VALUES (?, ?, ?, ?)",
            (email, hashed_password, role, company_id)
        )
        conn.commit()
        print(f"Successfully registered {email} (Role: {role}, Company ID: {company_id})")
    except sqlite3.IntegrityError:
        print(f"Error: User {email} is already registered.")
    except Exception as e:
        print(f"An error occurred: {e}")
    finally:
        if conn:
            conn.close()

if __name__ == "__main__":
    print("--- Console Registration Tool ---")
    email = input("Email: ").strip()
    password = input("Password: ").strip()
    role = input("Role (employee/recruiter): ").strip().lower()
    company_id = input("Company ID (optional): ").strip()
    
    if not email or not password or role not in ['employee', 'recruiter']:
        print("Invalid input. Please provide email, password, and a valid role.")
    else:
        register_user(email, password, role, company_id if company_id else None)
