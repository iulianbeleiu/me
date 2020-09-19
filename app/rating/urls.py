from django.urls import path, include
from rest_framework.routers import DefaultRouter

from .views import RatingViewSet


router = DefaultRouter()
router.register('rating', RatingViewSet)

app_name = 'rating'

urlpatterns = [
    path('', include(router.urls))
]
