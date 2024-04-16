from django.urls import path
from . import views

app_name = 'rooms'

urlpatterns = [
    path('', views.RoomListView.as_view(), name='room_list'),
    path('room/<str:room_name>/', views.RoomDetailView.as_view(), name='room_detail'),
]