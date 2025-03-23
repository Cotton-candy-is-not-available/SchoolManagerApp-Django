from django.contrib import admin

# Register your models here.

from .models import TD_list, Task, Event, JournalEntry

admin.site.register(TD_list)
admin.site.register(Task)
admin.site.register(Event)
admin.site.register(JournalEntry)
