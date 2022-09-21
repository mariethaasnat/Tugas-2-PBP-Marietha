from django.db import models

class WatchlistItem(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length = 25)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()