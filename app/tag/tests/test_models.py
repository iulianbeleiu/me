from django.test import TestCase
from django.contrib.auth import get_user_model
from tag.models import Tag


def sample_user(user_name='test.test', password='test123'):
    """Create a sample user"""
    return get_user_model().objects.create_user(user_name, password)


class ModelTests(TestCase):

    def test_tag_str(self):
        """Test the tag string representation"""
        tag = Tag.objects.create(user=sample_user(), name='Vegan')

        self.assertEqual(str(tag), tag.name)
