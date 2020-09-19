from django.db import models
from user.models import User


class Rating(models.Model):
    """Rating model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    stars = models.IntegerField(default=5)
    review = models.TextField(blank=True)
    author = models.CharField(max_length=255, default="Anonim")
    created = models.DateField(auto_now_add=True)
    updated = models.DateField(auto_now=True)

    def save(self, *args, **kwargs):
        if not self.stars:
            raise ValueError("Please provide rating stars value!")
        super(Rating, self).save(*args, **kwargs)
