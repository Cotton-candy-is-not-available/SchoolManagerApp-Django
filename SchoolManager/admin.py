from django.contrib import admin

# Register your models here.

from .models import Logs, Goal, Event, Calendar

admin.site.register(Logs)
admin.site.register(Goal)
admin.site.register(Event)
admin.site.register(Calendar)
