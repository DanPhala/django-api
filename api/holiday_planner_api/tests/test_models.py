import django
import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'api.settings')
django.setup()

import pytest
from holiday_planner_api.models import Destination

@pytest.mark.django_db
def test_destination_creation():
    destination = Destination.objects.create(
        name="New York",
        latitude=40.7128,
        longitude=-74.0060,
        start_date="2023-01-01",
        end_date="2023-01-02",
    )
    assert destination.name == "New York"
    assert destination.latitude == 40.7128
    assert destination.longitude == -74.0060
    assert str(destination.start_date) == "2023-01-01"
    assert str(destination.end_date) == "2023-01-02"
