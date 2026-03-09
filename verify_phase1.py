import unittest
import sys
import os
sys.path.append(os.path.join(os.path.dirname(__file__), 'hiring_platform'))
from app import create_app
from database import init_db, close_db
from config import Config
import os

class Phase1TestCase(unittest.TestCase):
    def setUp(self):
        self.db_path = 'test_database.sqlite'
        self.app = create_app({
            'TESTING': True,
            'DATABASE': self.db_path,
            'SECRET_KEY': 'test-key'
        })
        self.client = self.app.test_client()
        
        # Override Config.DATABASE temporarily for init_db
        original_db = Config.DATABASE
        Config.DATABASE = self.db_path
        init_db()
        Config.DATABASE = original_db

    def tearDown(self):
        if os.path.exists(self.db_path):
            os.remove(self.db_path)

    def register(self, email, password, role, company_id=None):
        return self.client.post('/auth/register', data=dict(
            email=email,
            password=password,
            role=role,
            company_id=company_id
        ), follow_redirects=True)

    def login(self, email, password):
        return self.client.post('/auth/login', data=dict(
            email=email,
            password=password
        ), follow_redirects=True)

    def logout(self):
        return self.client.get('/auth/logout', follow_redirects=True)

    def test_registration_and_login(self):
        # 1. Register employee with company_id
        rv = self.register('employee@test.com', 'pwd123', 'employee', 'COMP99')
        assert b'Login' in rv.data
        
        # 2. Duplicate email blocked
        rv = self.register('employee@test.com', 'pwd456', 'employee')
        assert b'is already registered' in rv.data

        # 3. Login success and session check
        rv = self.login('employee@test.com', 'pwd123')
        assert b'Employee Dashboard' in rv.data
        with self.client.session_transaction() as sess:
            assert sess['company_id'] == 'COMP99'

        # 4. Wrong password rejected
        self.logout()
        rv = self.login('employee@test.com', 'wrong')
        assert b'Incorrect password' in rv.data

    def test_role_based_access(self):
        # Register both
        self.register('emp@test.com', 'pwd', 'employee')
        self.register('rec@test.com', 'pwd', 'recruiter')

        # Login as employee
        self.login('emp@test.com', 'pwd')
        
        # Try to access recruiter dashboard
        rv = self.client.get('/recruiter_dashboard', follow_redirects=True)
        assert b'Access denied: recruiter role required' in rv.data
        assert b'Employee Dashboard' in rv.data # Redirected back

        self.logout()

        # Login as recruiter
        self.login('rec@test.com', 'pwd')
        
        # Try to access employee dashboard
        rv = self.client.get('/employee_dashboard', follow_redirects=True)
        assert b'Access denied: employee role required' in rv.data
        assert b'Recruiter Dashboard' in rv.data # Redirected back

    def test_logout_clears_session(self):
        self.register('test@test.com', 'pwd', 'employee')
        self.login('test@test.com', 'pwd')
        self.logout()
        
        rv = self.client.get('/employee_dashboard', follow_redirects=True)
        assert b'Login' in rv.data # Redirected to login

if __name__ == '__main__':
    unittest.main()
