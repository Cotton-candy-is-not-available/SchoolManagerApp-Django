from django.urls import path, include
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [

    #------- START PAGE -----#
    path('', views.start_page, name='start_page'),

#------ HOME PAGE ----#
    path('index/', views.index, name='index'),

#-------- CALENDAR -------#

    path('calendar/', views.calendar, name='calendar'),

# ------- REGISTER PAGE -------#
    path('register/', views.register, name='register'),

# -------- lOG IN ---------#

    path('login/', views.log_in, name='log_in'),


#--------- LOG OUT ------#
    path('user_logout', views.user_logout, name='user_logout'),


#------------ Events ------------#
    path('event-form/', views.addEvent, name="add_event"),


#--------- WEEKLY SCHEDULE --------#
    path('weekly_schedule/', views.weekly_schedule, name='weekly_schedule'),
    # path('weekly_schedule/', views.weekly_schedule, name='weekly_schedule'),

    # path('weekly_schedule/', views.counter, name='counter'),

]
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


