from django.urls import path
from . import views
from .views import displayEvents

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.calendar, name='calendar'),
    path('event-form/',views.addEvent, name="add_event"),
    path('displayEvents/', views.displayEvents, name="display_events"),
]