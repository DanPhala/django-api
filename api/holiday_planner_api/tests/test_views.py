# import pytest
# from rest_framework import status
# from rest_framework.test import APIClient
# from django.urls import reverse
# from holiday_planner_api.models import Destination

# @pytest.mark.django_db
# class TestDestinationAPI:
#     client = APIClient()

#     def test_create_destination(self):
#         url = reverse('destination-list-create')  # Replace with your actual URL name
#         data = {
#             "name": "New York, Pretoria, Joburg",
#             "start_date": "2024-10-01",
#             "end_date": "2024-10-07"
#         }

#         response = self.client.post(url, data, format='json')
#         assert response.status_code == status.HTTP_201_CREATED  # Adjust based on your response code
#         assert "weather_data" in response.data  # Check the response structure

#     def test_delete_all_destinations(self):
#         # Manually create some Destination records
#         Destination.objects.create(name="New York", country="USA", latitude=40.7128, longitude=-74.0060) # pylint: disable=no-member
#         Destination.objects.create(name="Pretoria", country="South Africa", latitude=-25.7479, longitude=28.2293) # pylint: disable=no-member

#         url = reverse('destination-list-create')  # Adjust to your actual URL pattern
#         response = self.client.delete(url)

#         assert response.status_code == status.HTTP_204_NO_CONTENT
#         assert Destination.objects.count() == 0  # Ensure all records were deleted
