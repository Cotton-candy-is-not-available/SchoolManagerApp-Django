from django.urls import path, include
from . import views
from .views import displayEvents

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # ------- START PAGE -----#
    path('', views.start_page, name='start_page'),


    # -------- CALENDAR -------#

    path('calendar/', views.calendar, name='calendar'),

    # ------- REGISTER PAGE -------#
    path('register/', views.register, name='register'),

    # -------- lOG IN ---------#

    path('login/', views.log_in, name='log_in'),

    # --------- LOG OUT ------#
    path('user_logout', views.user_logout, name='user_logout'),


    # --------- Todo_list: Tasks ------#
    path('create_goal', views.create_goal, name='create_goal'),
    path('toggle/<int:goal_id>/', views.Toggle_task, name='Toggle_task'),
    # delete goal from database
    path('delete_goal/<str:pk>', views.delete_goal, name='delete_goal'),

    # --------- Todo_list ------#
    path('FutureLogsGoals/', views.FutureLogsGoals, name='FutureLogsGoals'),
    path('create_logs/', views.create_logs, name='create_logs'),
    # delete list and all of its tasks from database
    path('delete_log/<str:pk>', views.delete_log, name='delete_log'),

    path('update_log_name/<str:pk>', views.update_log_name, name='update_log_name'),

    # ------------ Events ------------#
    path('add_Event/', views.addEvent, name="add_event"),
    path('viewEvent/<str:pk>', views.viewEvent, name="viewEvent"),
    path('updateEvent/<str:pk>', views.updateEvent, name='updateEvent'),

    #delete event from database
    path('deleteEvent/<str:pk>', views.deleteEvent, name='deleteEvent'),

    # --------- WEEKLY SCHEDULE --------#
    # path('weekly_schedule/<int:more_>', views.weekly_schedule, name='weekly_schedule'),
    path('back_to_weekly/', views.back_to_weekly, name='back_to_weekly'),
    path('weekly_schedule/', views.weekly_schedule, name='weekly_schedule'),
    path('next_/', views.next_, name='next_'),
    path('prev/', views.prev, name='prev'),

#------------ Events displaying in different ways --------------------------
    path('displayEvents/', views.displayEvents, name="display_events"),

    path('events_of_the_day/', views.events_of_the_day, name='events_of_the_day'),
    path('stayOnCurrentPage/', views.stayOnCurrentPage, name='stayOnCurrentPage'),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
