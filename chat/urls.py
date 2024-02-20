from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='group'),
    path('<slug:slug>/', views.chatroom, name='room'),
]