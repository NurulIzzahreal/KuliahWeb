from django.urls import path
from . import views

urlpatterns = [
    path('Izzah/', views.Izzah, name='Izzah'),
]