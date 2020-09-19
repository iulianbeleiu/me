from rest_framework import serializers
from .models import Rating


class RatingSerializer(serializers.ModelSerializer):
    """Serializer for rating"""

    class Meta():
        model = Rating
        fields = ('id', 'user', 'stars', 'review',
                  'author', 'created', 'updated')
