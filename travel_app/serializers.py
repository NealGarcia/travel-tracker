from rest_framework import serializers
from .models import Entry, Trip

class TripSerializer(serializers.HyperlinkedModelSerializer):
    entry = serializers.HyperlinkedRelatedField(
        view_name='entry_detail',
        many=True,
        read_only=True
    )
    class Meta:
        model = Trip
        fields = ('location', 'start_date', 'end_date', 'entry')

class EntrySerializer(serializers.HyperlinkedModelSerializer):
    trip = serializers.HyperlinkedRelatedField(
        view_name='trip_detail',
        many = False,
        read_only=True
    )
    class Meta:
        model = Entry
        fields = ('photo_url', 'body', 'date', 'trip')