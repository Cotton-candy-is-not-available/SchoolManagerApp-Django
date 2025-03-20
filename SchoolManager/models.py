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
    date_of_event = models.DateField(null = True, blank = True)

    def __str__(self):
        return f"{self.event_name},  on the {self.date_of_event}"


#------ To do list --------------
class TD_list(models.Model):
    List_name = models.CharField(max_length=100)
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, editable = False)
    def __str__(self):
        return self.List_name

class Task(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, null = True, editable = False)
    list = models.ForeignKey(TD_list, on_delete=models.CASCADE)
    description = models.CharField(max_length=100)
    completed = models.BooleanField(default=False)
    Important = models.BooleanField(default=False)
    mid_important = models.BooleanField(default=False)
    least_important = models.BooleanField(default=False)
    class Meta:
        ordering = ['-Important', '-mid_important', '-least_important']
    def __str__(self):
        return self.list.List_name + ": " + self.description


#
# class Event(models.Model):
#     date_of_event = models.DateField(null = True, blank = True)
#     description = models.TextField()
#     #each event can be associated to only one calendar
#
#     def __str__(self):
#         return f"Event on {self.date_of_event}"
