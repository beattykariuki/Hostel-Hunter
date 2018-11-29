from app .models import Review,User
from app import db

def setUp(self):
    self.user_beatty = User(username = 'beatty',password = '1205' email = 'bettykariuki@gmail.com')
    self.new_review = Review(hostel_id=12345,hostel_title='Review for hostels',image_path="https://image.tmdb.org/t/p/w500/jdjdjdjn",hostel_review='This hostel is the best thing since sliced bread',user = self.user_Beatty)

def tearDown(self):
    Review.query.delete()
    User.query.delete()

def test_check_instance_variables(self):
    self.assertEquals(self.new_review.hostel_id,12345)
    self.assertEquals(self.new_review.hostel_title,'Review for hostels')
    self.assertEquals(self)