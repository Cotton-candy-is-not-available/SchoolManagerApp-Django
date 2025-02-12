from django.urls import path
from . import views


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


#--------- WEEKLY SCHEDULE --------#
    path('weekly_schedule/', views.weekly_schedule, name='weekly_schedule'),

]



