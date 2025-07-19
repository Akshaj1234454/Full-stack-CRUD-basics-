from django.contrib import admin
from django.urls import path, include
from . import views
urlpatterns = [
    path('', views.dataApp, name='dataApp'),
    path('scrollPage/', views.scrollPage, name='scrollPage'),
    path('scrollPage/<int:srNo>/', views.editEntry, name='editEntry'),
]
