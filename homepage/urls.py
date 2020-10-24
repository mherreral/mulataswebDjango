from django.urls import path
from . import views

urlpatterns = [
    path('', views.suggest),
    path('addItem/', views.addItem),
]