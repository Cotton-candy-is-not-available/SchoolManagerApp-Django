from django.urls import path, include
from . import views
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

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)