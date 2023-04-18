from django.urls import path
from chat import views
from django.contrib import admin

urlpatterns = [
    path('', views.messages_page),
]
