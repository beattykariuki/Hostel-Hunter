<<<<<<< HEAD
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
=======
import unittest
from app.models import Review

class TestReview(unittest.TestCase):
    """
    This class  will test the reviews
    """

    def setUp(self):
        """
        This will create a new review before each test
        """
        self.new_review = Review(title = "Haha")

    def tearDown(self):
        """
        THis will clear the db after each test
        """
        Review.query.delete()

    def test_is_instance(self):
        """
        This will test whether the review created is an instance of the Review class
        """
        self.assertTrue(isinstance(self.new_review, Review))

    def test_init(self):
        """
        This willl test whether the new_review is instantiated correctly
        """
        self.assertTrue(self.new_review.title == "Haha")

    def test_save_review(self):
        """
        This will test whether the review is added to the db
        """
        self.new_review.save_review()
        self.assertTrue(len(Review.query.all()) > 0)
    
>>>>>>> review
