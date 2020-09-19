from django.test import TestCase, Client
from django.contrib.auth import get_user_model
from django.urls import reverse


class AdminSiteTests(TestCase):

    def setUp(self):
        self.client = Client()
        self.admin_user = get_user_model().objects.create_superuser(
            user_name='test.admin',
            password='adminpassword'
        )
        self.client.force_login(self.admin_user)
        self.user = get_user_model().objects.create_user(
            user_name='test.admin2',
            password='testpassword',
            name='User fullname'
        )

    def test_users_listed(self):
        """Test that users are listed on user page"""
        url = reverse('admin:user_user_changelist')
        res = self.client.get(url)

        self.assertContains(res, self.user.name)
        self.assertContains(res, self.user.user_name)

    def test_user_change_page(self):
        """Test that the user edit page works"""
        url = reverse('admin:user_user_change', args=[self.user.id])
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)

    def test_create_user_page(self):
        """Test that the create user page works"""
        url = reverse('admin:user_user_add')
        res = self.client.get(url)

        self.assertEqual(res.status_code, 200)
