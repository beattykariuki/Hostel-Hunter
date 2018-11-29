from . import db
from datetime import datetime


class Review(db.Model):

    __tablename__ = 'reviews'

    id = db.Column(db.Integer,primary_key = True)
    review_id = db.Column(db.Integer,db.ForeignKey('hostels.id'))
    review = db.Column(db.String())
    user_id = db.Column(db.Integer,db.ForeignKey('users.id'))
    posted = db.Column(db.DateTime,default=datetime.utcnow)

    
    def save_comment(self):

        db.session.add(self)
        db.session.commit()