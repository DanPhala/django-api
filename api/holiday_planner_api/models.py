from django.db import models

class Destination(models.Model):
    name = models.CharField(max_length=200)
    latitude = models.FloatField(default='0')
    longitude = models.FloatField(default='0')
    start_date = models.DateField(default='2023-01-01')
    end_date = models.DateField(default='2023-01-01')
    published_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)