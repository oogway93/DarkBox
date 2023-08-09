from django.urls import reverse
from rest_framework.test import APITestCase, APIRequestFactory
from rest_framework import status
from api.views import PhonesModelViewSet, LaptopsModelViewSet


class TestAPI(APITestCase):
    def test_get_data(self):
        self.assertTrue(PhonesModelViewSet.serializer_class)
        self.assertTrue(LaptopsModelViewSet.serializer_class)
        url = reverse('phone')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        response2 = self.client.get('/phones/1')
        self.assertEqual(response2.status_code, status.HTTP_404_NOT_FOUND)
