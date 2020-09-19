from django.test import TestCase
from django.contrib.auth import get_user_model
from rating.models import Rating


def sample_user(user_name='rating.test', password='rating123'):
    """Create sample user"""
    return get_user_model().objects.create_user(user_name, password)


class ModelTests(TestCase):

    def test_create_a_rating(self):
        """Test create a rating for an user"""
        rating = Rating.objects.create(
            user=sample_user(),
            stars=5,
            review="This is a test review",
        )

        self.assertEqual(5, rating.stars)

    def test_create_rating_invalid(self):
        """Test that stars are provide to the rating"""
        with self.assertRaises(ValueError):
            Rating.objects.create(
                user=sample_user('test.invalid', 'invalid123'),
                stars=None,
            )
