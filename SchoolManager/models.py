from django.db import models
import datetime

class Event(models.Model):
    event_name = models.CharField(max_length=100, default= "[Event Name]")#event name
    date_of_event = models.DateField(null = True, blank = True)#add start and end date
    description = models.TextField()
    #each event can be associated to only one calendar

    def __str__(self):
        return f"{self.event_name},  on the {self.date_of_event}"

