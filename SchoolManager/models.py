from django.db import models

class Calendar(models.Model): #each calendar can have many events associated to it
    date = models.DateField()
    def __str__(self):
        return str(self.date.day)

class Event(models.Model):
    start_time = models.TimeField()
    end_time = models.TimeField()
    description = models.TextField()
    #each event can be associated to only one calendar
    day = models.ForeignKey('Calendar', null=False, blank=False, on_delete=models.CASCADE, related_name='events')






