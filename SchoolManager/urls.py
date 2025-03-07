from django.urls import path, include
from . import views
from .views import displayEvents

from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    # ------- START PAGE -----#
    path('', views.start_page, name='start_page'),

    # ------ HOME PAGE ----#
    path('index/', views.index, name='index'),

    # -------- CALENDAR -------#

    path('calendar/', views.calendar, name='calendar'),

    # ------- REGISTER PAGE -------#
    path('register/', views.register, name='register'),

    # -------- lOG IN ---------#

    path('login/', views.log_in, name='log_in'),

    # --------- LOG OUT ------#
    path('user_logout', views.user_logout, name='user_logout'),


    # --------- Todo_list: Tasks ------#
    path('create_task', views.create_task, name='create_task'),
    path('toggle/<int:task_id>/', views.Toggle_task, name='Toggle_task'),
    # delete task from database
    path('delete_task/<str:pk>', views.delete_task, name='delete_task'),

    # --------- Todo_list ------#
    path('Todo_list/', views.Todo_list, name='Todo_list'),
    path('create_list/', views.create_list, name='create_list'),
    # delete list and all of its tasks from database
    path('delete_list/<str:pk>', views.delete_list, name='delete_list'),

    # path('update_list_name/<str:pk>', views.update_list_name, name='update_list_name'),

    # ------------ Events ------------#
    path('add_Event/', views.addEvent, name="add_event"),
    path('viewEvent/<str:pk>', views.viewEvent, name="viewEvent"),
    # path('updateEvent/<str:pk>', views.updateEvent, name='updateEvent'),

    #delete event from database
    path('deleteEvent/<str:pk>', views.deleteEvent, name='deleteEvent'),

    # --------- WEEKLY SCHEDULE --------#
    # path('weekly_schedule/<int:more_>', views.weekly_schedule, name='weekly_schedule'),
    path('weekly_schedule/', views.weekly_schedule, name='weekly_schedule'),
    path('next_/', views.next_, name='next_'),
    path('prev/', views.prev, name='prev'),

    # path('event-form/', views.addEvent, name="add_event"),
    path('displayEvents/', views.displayEvents, name="display_events"),
]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
