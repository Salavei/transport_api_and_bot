from rest_framework import serializers
from rest_framework.serializers import ModelSerializer
from .models import SelectedTransport, SelectedStation

class TransportSerializer(ModelSerializer):
    name_transport = serializers.CharField()
    number_transport = serializers.CharField()

    class Meta:
        model = SelectedTransport
        fields = ('name_transport', 'number_transport')


class StationSerializer(ModelSerializer):
    name_transport = serializers.CharField()
    number_transport = serializers.CharField()
    station = serializers.CharField()

    class Meta:
        model = SelectedStation
        fields = ('name_transport', 'number_transport', 'station')