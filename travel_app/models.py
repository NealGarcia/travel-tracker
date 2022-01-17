from tokenize import Triple
from django.db import models

class Trip(models.Model):
    location = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.location

class Entry(models.Model):
    photo_url = models.TextField()
    body = models.TextField()
    date = models.DateField()
    trip = models.ForeignKey(Trip, on_delete=models.CASCADE, related_name = 'entry')

    def __str__(self):
        return str(self.date)

# Create your models here.
