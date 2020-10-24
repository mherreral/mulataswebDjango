from django.urls import path
from . import views

urlpatterns = [
    path('test/', views.send),
    path('grade/', views.grade)
]