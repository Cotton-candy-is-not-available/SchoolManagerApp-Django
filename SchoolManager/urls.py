from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('calendar/', views.calendar, name='calendar'),

# register page
    path('register/', views.register, name='register'),

# log in

    path('login/', views.login, name='login'),
]






