from django.db import models
from unicodedata import decimal

class WatchlistItem(models.Model):
    watched = models.BooleanField()
    title = models.CharField(max_length = 25)
    # rating = models.DecimalField(max_digits = 5, decimal_places = 1)
    rating = models.FloatField()
    release_date = models.DateField()
    review = models.TextField()