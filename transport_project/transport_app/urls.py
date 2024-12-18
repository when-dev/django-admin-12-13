from django.urls import path
from . import views

urlpatterns = [
    path('', views.vehicle_list, name='vehicle_list'),
    path('add_vehicle/', views.add_vehicle, name='add_vehicle'),
    path('add_owner/', views.add_owner, name='add_owner'),
    path('add_ownership/', views.add_ownership, name='add_ownership'),
]

