from django.db import models

class Event(models.Model):
    date_of_event = models.DateField(null = True, blank = True)
    description = models.TextField()
    #each event can be associated to only one calendar

    def __str__(self):
        return f"Event on {self.date_of_event}"
