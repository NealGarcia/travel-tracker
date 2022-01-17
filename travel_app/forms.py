from django import forms
from .models import Trip, Entry

class TripForm(forms.ModelForm):
    class Meta:
        model = Trip
        fields = ('location', 'start_date', 'end_date',)

class EntryForm(forms.ModelForm):
    class Meta:
        model = Entry
        fields = ('photo_url', 'body', 'date', 'tripEntry',)