from django.shortcuts import render
from .models import ChatRoom, ChatMessage

# Create your views here.

def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chat/index.html', {'chatrooms':chatrooms})

def chatroom(request, slug):
    room = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=room)
    return render(request, 'chat/room.html', {'room':room, 'messages':messages})