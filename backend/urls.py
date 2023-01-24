from django.contrib import admin
from django.urls import path,include
from . import views

urlpatterns = [
    path('teams/', views.get_teams),
    path('eventshappened/', views.get_eventshappened),
    path('upcommingevents/', views.get_upcommingevents),
]