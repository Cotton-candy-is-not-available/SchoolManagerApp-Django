from django.contrib.auth.models import User
from django.db import models

class Event(models.Model):
    # Start_time = models.DateTimeField(null=True, blank=True)
    # End_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, editable = False)
    event_name = models.CharField(max_length=100, default= "[Event Name]")#event name
    description = models.TextField()
    date_of_event = models.DateField(null = True, blank = True)
    del_ete = models.BooleanField(default=False)

    # Move to, to do list tasks
    # Important = models.BooleanField(default=False)
    # mid_important = models.BooleanField(default=False)
    # least_important = models.BooleanField(default=False)
    # each event can be associated to only one calendar
    # class Meta:
    #     ordering = ['-Important', '-mid_important', '-least_important']

    def __str__(self):
        return f"{self.event_name},  on the {self.date_of_event}"

