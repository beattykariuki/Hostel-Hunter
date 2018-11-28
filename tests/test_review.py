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
    
