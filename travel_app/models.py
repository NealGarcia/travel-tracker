from django.db import models

class TripEntry(models.Model):
    location = models.CharField(max_length = 50)
    start_date = models.DateField()
    end_date = models.DateField()

    def __str__(self):
        return self.name

class EntryDetail(models.Model):
    photo_url = models.TextField()
    body = models.TextField()
    date = models.DateField()
    tripEntry = models.ForeignKey(TripEntry, on_delete=models.CASCADE, related_name = 'entryDetails')

    def __str__(self):
        return self.date

# Create your models here.
