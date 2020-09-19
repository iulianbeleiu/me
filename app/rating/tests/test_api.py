from django.urls import reverse
from django.test import TestCase
from django.contrib.auth import get_user_model

from rest_framework import status
from rest_framework.test import APIClient

from rating.models import Rating
from rating.serializer import RatingSerializer


RATINGS_URL = reverse('rating:rating-list')


def user_rating_url(user_id):
    """Generate user id url"""
    return reverse('rating:rating-detail', args=[user_id])


class RatingApiTest(TestCase):
    """Testing rating api"""

    def setUp(self):
        self.client = APIClient()
        self.user = get_user_model().objects.create_user(
            user_name='rating.api',
            password='api12345',
        )

    def test_retrieve_ratings(self):
        """Test retrieving all ratings"""
        Rating.objects.create(
            user=self.user,
            stars=4,
            review='Test review api',
        )
        Rating.objects.create(
            user=self.user,
            stars=5,
        )

        res = self.client.get(RATINGS_URL)

        ratings = Rating.objects.all()
        serializer = RatingSerializer(ratings, many=True)

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data, serializer.data)

    def test_retrieve_ratings_by_user(self):
        """Test retrieving ratings only for specific user"""
        rating = Rating.objects.create(
            user=self.user,
            stars=2
        )
        Rating.objects.create(
            user=get_user_model().objects.create_user(
                user_name='user.rating2',
                password='rating232131'
            ),
            stars=5,
        )

        res = self.client.get(user_rating_url(rating.id))

        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(res.data['user'], self.user.id)
        self.assertEqual(res.data['stars'], rating.stars)

    def test_create_rating(self):
        """Test creating a rating for user"""
        payload = {
            'user': self.user.id,
            'stars': 5
        }

        res = self.client.post(RATINGS_URL, payload)

        self.assertEqual(res.status_code, status.HTTP_201_CREATED)

        exists = Rating.objects.filter(
            user=self.user,
            stars=payload['stars']
        ).exists()

        self.assertTrue(exists)
