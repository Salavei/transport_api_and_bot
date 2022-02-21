from django.shortcuts import render
from ugc.serializers import TransportSerializer, StationSerializer
# Create your views here.
from rest_framework import mixins, status
from rest_framework.viewsets import ReadOnlyModelViewSet, GenericViewSet
from rest_framework.response import Response

from ugc.management.commands.parser import parser_all_station, parser_station_n


class TransportSerializerView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = TransportSerializer

    def create(self, request, *args, **kwargs):
        print(self.request.data['name_transport'])
        print(self.request.data['number_transport'])
        return Response(parser_all_station(self.request.data['name_transport'], self.request.data['number_transport']),
                        status=status.HTTP_201_CREATED)


class StationSerializerView(mixins.CreateModelMixin, GenericViewSet):
    serializer_class = StationSerializer

    def create(self, request, *args, **kwargs):
        print(self.request.data['name_transport'])
        print(self.request.data['number_transport'])
        print(self.request.data['station'])
        return Response(parser_station_n(self.request.data['name_transport'], self.request.data['number_transport'],
                                         self.request.data['station']),
                        status=status.HTTP_201_CREATED)
