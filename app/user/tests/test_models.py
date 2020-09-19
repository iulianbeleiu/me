from django.test import TestCase
from django.contrib.auth import get_user_model


class ModelTests(TestCase):

    def test_create_user_with_username_successful(self):
        """Test creating a new user with an user name is successful"""
        user_name = 'test.test'
        password = 'test123'
        user = get_user_model().objects.create_user(
            user_name=user_name,
            password=password
        )

        self.assertEqual(user.user_name, user_name)
        self.assertTrue(user.check_password(password))

    def test_create_user_invalid_user_name(self):
        """Test creating a user with no user name raises error"""
        with self.assertRaises(ValueError):
            get_user_model().objects.create_user(None, 'test123')

    def test_create_new_superuser(self):
        """Test creating a new superuser"""
        user = get_user_model().objects.create_superuser(
            'test.test1',
            'test123'
        )

        self.assertTrue(user.is_superuser)
        self.assertTrue(user.is_staff)
