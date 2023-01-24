from rest_framework.test import APITestCase
from rest_framework.status import HTTP_200_OK
from django.urls import reverse
from bot_app.management.commands.parser import parser_station_n, parser_all_station
from bot_app.serializers import TransportSerializer, StationSerializer
import json


class TransportApiTestCase(APITestCase):
    def test_successful_get_transport_information(self):
        url = reverse('infotrans-list')
        data = {
            "transport_type": "Автобус",
            "transport_number": "24"
        }
        json_data = json.dumps(data)

        serialized_data = TransportSerializer(data=data, many=False)
        self.assertTrue(serialized_data.is_valid(raise_exception=True))
        data_about_transport = parser_all_station(
            transport=data.get('transport_type'),
            number_transport=data.get('transport_number')
        )

        response = self.client.post(url, data=json_data, content_type='application/json')
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(data_about_transport, response.data)


class StationApiTestCase(APITestCase):

    def test_successful_get_station_information(self):
        url = reverse('infostation-list')
        data = {
            "transport_type": "Автобус",
            "transport_number": "24",
            "station": "Мирошниченко"
        }
        json_data = json.dumps(data)
        serialized_data = StationSerializer(data=data, many=False)
        self.assertTrue(serialized_data.is_valid())
        response = self.client.post(url, data=json_data, content_type='application/json')
        data_about_station = parser_station_n(
            transport=data.get('transport_type'),
            number_transport=data.get('transport_number'),
            station=data.get('station')
        )
        self.assertEqual(HTTP_200_OK, response.status_code)
        self.assertEqual(data_about_station, response.data)


class SerializerApiTestCase(APITestCase):
    def test_serializer_error_transport_information(self):
        exception_data_first = {

        }
        serialized_data = TransportSerializer(data=exception_data_first, many=False)
        self.assertFalse(serialized_data.is_valid())

        exception_data_second = {
            "qwer": "Автобус",
            "1234": "24"
        }
        serialized_data = TransportSerializer(data=exception_data_second, many=False)
        self.assertFalse(serialized_data.is_valid())

    def test_serializer_error_station_information(self):
        exception_data_first = {

        }
        serialized_data = StationSerializer(data=exception_data_first, many=False)
        self.assertFalse(serialized_data.is_valid())

        exception_data_second = {
            "qwer": "Автобус",
            "1234": "24"
        }
        serialized_data = StationSerializer(data=exception_data_second, many=False)
        self.assertFalse(serialized_data.is_valid())

        exception_data_third = {
            "qwer": "Автобус",
            "1234": "24",
            "asfsf": "fsafsf"
        }
        serialized_data = StationSerializer(data=exception_data_third, many=False)
        self.assertFalse(serialized_data.is_valid())
