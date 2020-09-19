from rest_framework import viewsets

from .models import Rating

from .serializer import RatingSerializer


class RatingViewSet(viewsets.ModelViewSet):

    queryset = Rating.objects.all()
    serializer_class = RatingSerializer
