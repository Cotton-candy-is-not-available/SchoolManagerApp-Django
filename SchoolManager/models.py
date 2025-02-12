from django.db import models

# Create your models here.

class Calendar(models.Model): #each calendar can have many events associated to it
    date = models.DateField()
    day_number = models.IntegerField()
    text_box = models.TextField(null=True, blank=True)

class Event(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    #each event can be associated to only one calendar
    calendar = models.ForeignKey('Calendar', null=False, blank=False, on_delete=models.CASCADE, related_name='events')






