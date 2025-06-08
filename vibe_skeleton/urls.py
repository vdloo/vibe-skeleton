"""vibe_skeleton URL Configuration
"""
from django.contrib import admin
from django.urls import path
from vibe_app import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('some_model/', views.some_response, name='some_model'),
]
