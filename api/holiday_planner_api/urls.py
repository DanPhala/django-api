from django.urls import path
from . import views

urlpatterns = [
    path('destination/', views.DestinationListCreate.as_view(), name='destination-list-create'),
]
