import os
import pytest

os.environ['DJANGO_SETTINGS_MODULE'] = 'api.settings'
pytestmark = pytest.mark.django_db
