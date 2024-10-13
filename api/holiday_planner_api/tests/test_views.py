import os
import django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

import pytest
from rest_framework import status
from rest_framework.test import APIClient
from django.urls import reverse
from holiday_planner_api.models import Destination

@pytest.mark.django_db
class TestDestinationAPI:
    client = APIClient()

    def test_create_destination(self):
        url = reverse('destination-list-create')
        data = {
            "name": "New York, Pretoria, Joburg",
            "start_date": "2024-10-01",
            "end_date": "2024-10-07"
        }
        response = self.client.post(url, data, format='json')
        assert response.status_code == status.HTTP_200_OK 
    def test_delete_all_destinations(self):
        Destination.objects.create(name="New York", latitude=40.7128, longitude=-74.0060)
        Destination.objects.create(name="Pretoria", latitude=-25.7479, longitude=28.2293)
        
        url = reverse('destination-list-create')
        response = self.client.delete(url)
        assert response.status_code == status.HTTP_204_NO_CONTENT
