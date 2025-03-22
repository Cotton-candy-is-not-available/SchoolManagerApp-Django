from django.contrib.auth.models import User
from django.db import models


#------ Calendar --------------
class Calendar(models.Model): #each calendar can have many events associated to it
    date = models.DateField()
    day_number = models.IntegerField()
    text_box = models.TextField(null=True, blank=True)

#------ Events --------------
class Event(models.Model):
    # Start_time = models.DateTimeField(null=True, blank=True)
    # End_time = models.DateTimeField(null=True, blank=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, editable = False)
    event_name = models.CharField(max_length=100, default= "[Event Name]")#event name
    description = models.TextField()
    date_of_event = models.DateField()

    def __str__(self):
        return f"{self.event_name},  on the {self.date_of_event}"


#------ Future logs and goals --------------
# logs
class Logs(models.Model):
    Log_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, editable = False)
    def __str__(self):
        return self.Log_name
# goals
class Goal(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, editable = False)
    log = models.ForeignKey(Logs, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)

    Order = [
        ("1", "Very Important"),
        ("2", "Mildly Important"),
        ("3", "Least Important"),
    ]
    Importance = models.CharField(choices=Order, default="1", max_length=50)

    class Meta:
        ordering = ['Importance']
    def __str__(self):
        return self.log.Log_name + ": " + self.description
