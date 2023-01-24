from bot_app.serializers import TransportSerializer, StationSerializer
from rest_framework import status
from rest_framework.viewsets import GenericViewSet
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response
from bot_app.management.commands.parser import parser_all_station, parser_station_n
from bot_app.models import SelectedTransport, SelectedStation


class TransportView(CreateModelMixin, GenericViewSet):
    queryset = SelectedTransport.objects.all()
    serializer_class = TransportSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(parser_all_station(self.request.data['transport_type'], self.request.data['transport_number']),
                        status=status.HTTP_200_OK,
                        headers=headers)


class StationView(CreateModelMixin, GenericViewSet):
    queryset = SelectedStation.objects.all()
    serializer_class = StationSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        headers = self.get_success_headers(serializer.data)
        return Response(parser_station_n(self.request.data['transport_type'], self.request.data['transport_number'],
                                         self.request.data['station']), status=status.HTTP_200_OK,
                        headers=headers)