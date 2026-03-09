"""Quick SMTP diagnostic script."""
import smtplib
from email.mime.text import MIMEText

SERVER   = 'smtp.gmail.com'
PORT     = 587
USERNAME = 'q2494301@gmail.com'
PASSWORD = 'ztfd ljgy ihyn nbbz'   # with spaces
TO_EMAIL = '2025021345@mmmut.ac.in'

print(f"[1] Connecting to {SERVER}:{PORT} ...")
try:
    smtp = smtplib.SMTP(SERVER, PORT, timeout=15)
    print("[2] Connected. Starting TLS ...")
    smtp.starttls()
    print("[3] TLS OK. Logging in ...")
    smtp.login(USERNAME, PASSWORD)
    print("[4] Login OK! Sending test email ...")

    msg = MIMEText("This is a test email from AI Hiring Platform.")
    msg['Subject'] = 'SMTP Test'
    msg['From'] = USERNAME
    msg['To'] = TO_EMAIL
    smtp.sendmail(USERNAME, TO_EMAIL, msg.as_string())
    print("[5] Email sent successfully!")
    smtp.quit()
except Exception as e:
    print(f"FAILED at step above: {type(e).__name__}: {e}")
