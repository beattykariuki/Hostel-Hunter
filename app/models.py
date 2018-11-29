<<<<<<< HEAD
<<<<<<< HEAD
from . import db 
from werkzeug.security import generate_password_hash,check_password_hash
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id)

class User(UserMixin,db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer,primary_key = True)
    username = db.Column(db.String(255)),index = True)
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer,db.Foreinkey('roles.id'))
    bio = db.Column(db.string(255))
    profile_pic_path = db.Clomun(db.String())
    password_secure = db.Column(db.String(255))
    password_hash = db.Column(db.String(255))

    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")


    def __repr__(self):
        return f'User {self.username}' 


pass_secure = db.Column(db.String(255))


class Review(db.Model):
    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    hostel_id = db.Column(db.Integer)
    hostel_title = db.Column(db.String)
    image_path = db.Column(db.String)
    hostel_review = db.Column(db.String)
    posted = db.Column(db.DateTime,default=datetime.utcnow)
    user_id =db.Column(db.Integer,db.Foreinkey("users.id"))

    def save_review(self):
        db.session.add(self)
        db.sessin.commit()

    @classmethod
    def get_reviews(cls,id):
        reviews = Review.query.filter_by(movie_id=id).a11()
        return reviews


    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self,password):
        self.pass_secure = generate_password_hash(password)

    def verify_pssword(self,password):
        return check_password_hash(self.pass_secure,password)

        pass_secure = db.Column(db.String(255))


class Role(db.Model):
    __tablename__ = 'roles'

    id = db.Column(db.Integer,primary_key = True)
    name = db.Column(db.String(255))
    users = db.relationship('User',backref = 'role',lazy = "dynamic")

    def __repr__(self):
        return f'User {self.name}' 
    
=======
from . import db
from datetime import datetime

class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    # hostel_id = db.Column(db.Integer,db.ForeignKey('hostels.id'))
    review = db.Column(db.String())
    # user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    
    def save_comment(self):

        db.session.add(self)
        db.session.commit()
>>>>>>> review
=======
from . import db

class University:
    def __init__(self,id,name,content):
        self.id =id
        self.name = name
        self.content = content
        self.image= 'https://4.bp.blogspot.com/-cpnu-2lNOCM/W0XKYTx8V_I/AAAAAAAABBo/4XsF2n1eWRMiBTjOXu7_WsjD2OtDPKvWQCLcBGAs/s1600/images%2B%252822%2529.jpg'




        
>>>>>>> searchHostel
