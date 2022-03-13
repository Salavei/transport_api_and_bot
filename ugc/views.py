from ugc.serializers import TransportSerializer, StationSerializer
from rest_framework import status
from rest_framework.viewsets import ViewSet
from rest_framework.response import Response
from ugc.management.commands.parser import parser_all_station, parser_station_n


class TransportSerializerView(ViewSet):
    serializer_class = TransportSerializer

    def create(self, request, *args, **kwargs):
        if 'transport_type' not in request.data or request.data.get('transport_type') == '':
            return Response(['Transport type field is required.'], status=400)
        elif 'transport_number' not in request.data or request.data.get('transport_number') == '':
            return Response(['Transport number field is required.'], status=400)
        return Response(parser_all_station(self.request.data['transport_type'], self.request.data['transport_number']),
                        status=status.HTTP_200_OK)


class StationSerializerView(ViewSet):
    serializer_class = StationSerializer

    def create(self, request, *args, **kwargs):
        if 'transport_type' not in request.data or request.data.get('transport_type') == '':
            return Response(['Transport type field is required.'], status=400)
        elif 'transport_number' not in request.data or request.data.get('transport_number') == '':
            return Response(['Transport number field is required.'], status=400)
        elif 'station' not in request.data or request.data.get('station') == '':
            return Response(['Station number field is required.'], status=400)
        return Response(parser_station_n(self.request.data['transport_type'], self.request.data['transport_number'],
                                         self.request.data['station']),
                        status=status.HTTP_200_OK)
