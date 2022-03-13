from rest_framework.serializers import ModelSerializer
from .models import SelectedTransport, SelectedStation


class TransportSerializer(ModelSerializer):
    class Meta:
        model = SelectedTransport
        fields = ('transport_type', 'transport_number')


class StationSerializer(ModelSerializer):
    class Meta:
        model = SelectedStation
        fields = ('transport_type', 'transport_number', 'station')
