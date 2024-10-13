from rest_framework.response import Response
from holiday_planner_api.models import Destination

def delete_all_destinations(request):
    """Delete all destination records."""
    Destination.objects.all().delete()  # pylint: disable=no-member
    return Response(status=204)
