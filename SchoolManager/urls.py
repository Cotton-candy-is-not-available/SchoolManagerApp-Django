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

# --------- Todo_list ------#
    path('create_task', views.create_task, name='create_task'),

# --------- Todo_list ------#
    path('Todo_list/', views.Todo_list, name='Todo_list'),
    path('create_list/', views.create_list, name='create_list'),

    # path('update_list_name/<str:pk>', views.update_list_name, name='update_list_name'),
    # path('delete_list/<str:pk>', views.delete_list, name='delete_list'),

]




