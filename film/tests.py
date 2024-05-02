from django.http import HttpResponse
from django.test import TestCase
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status


# Create your tests here.

class FilmListTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.url = reverse('api:film:get-all')

    def test_normal(self) -> None:
        response: HttpResponse = self.client.get(self.url, format='json')

        print(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FilmDetailTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.id_tayangan = 1
        self.url = reverse('api:film:get-detail', args=[self.id_tayangan])

    def test_normal(self) -> None:
        response: HttpResponse = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)


class FilmUlasanTest(TestCase):
    def setUp(self) -> None:
        self.client = APIClient()
        self.id_tayangan = 2
        self.url = reverse('api:film:get-reviews', args=[self.id_tayangan])

    def test_normal(self) -> None:
        response: HttpResponse = self.client.get(self.url, format='json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)
