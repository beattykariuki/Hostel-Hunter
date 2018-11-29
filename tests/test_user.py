import unnitest
from app.models import User

class UserModelTest(unnitest.TestCase):

    def setUp(self):
        self.new_user = User(password = 'mypassword')

    def test_password_setter(self):
        self.assertTrue(self.new_user.pass_secure is not None)

    def test_no_access_password(self):
        with self.asserRaises(AttributeError):
            self.new_user.password

    def test_password_verification(self):
        self.assertTrue(self.new_user.verify_password('mypassword'))