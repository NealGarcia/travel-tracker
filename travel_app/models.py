from django.db import models

class TripEntry(models.Model):
    location = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

# Create your models here.
