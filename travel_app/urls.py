from django.urls import path
from . import views
from rest_framework.routers import DefaultRouter


urlpatterns = [
    path('trips/', views.TripList.as_view(), name = 'trip_list'),
    path('trips/<int:pk>', views.TripDetail.as_view(), name = 'trip_detail'),
    path('entries/', views.EntryList.as_view(), name = 'entry_list'),
    path('entries/<int:pk>', views.EntryDetail.as_view(), name = 'entry_detail'),

]