from django.urls import path
from . import views

urlpatterns = [
    # Trips
    path('', views.trip_list, name = 'trip_list'),
    path('trips/new', views.trip_create, name = 'trip_create'),
    path('trips/<int:pk>', views.trip_detail, name = 'trip_detatil'),
    path('trips/<int:pk>/edit', views.trip_edit, name = 'trip_edit'),
    path('trips/<int:pk>/delete', views.trip_delete, name = 'trip_delete'),

    # Entry Details
    path('', views.entry_list, name = 'entry_list'),
    path('entry/new', views.entry_create, name = 'entry_create'),
    path('entry/<int:pk>', views.entry_detail, name = 'entry_detail'),
    path('entry/<int:pk>/edit', views.entry_edit, name = 'entry_edit'),
    path('entry/<int:pk>/delete', views.entry_delete, name = 'entry_delete'),
]