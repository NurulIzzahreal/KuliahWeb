from django.urls import include, path
from . import views

urlpatterns = [
    path('members/', views.members, name='members'),
]