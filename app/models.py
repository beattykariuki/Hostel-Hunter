from . import db 
<<<<<<< HEAD
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
    
=======

>>>>>>> authentication
class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255))
<<<<<<< HEAD
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.Foreinkey('roles.id'))
    password_hash = db.Column(db.String(255))
=======
    role_id = db.Column(db.Integer,db.Foreinkey('roles.id'))
>>>>>>> authentication

    def __repr__(self):
        return f'User {self.username}' 

<<<<<<< HEAD
pass_secure = db.Column(db.String(255))

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_pssword(self,password):
        return check_password_hash(self.pass_secure,password)

=======
        pass_secure = db.Column(db.String(255))
>>>>>>> authentication


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.name}' 
    