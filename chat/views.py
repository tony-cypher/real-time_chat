from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import ChatRoom, ChatMessage

# Create your views here.

@login_required
def index(request):
    chatrooms = ChatRoom.objects.all()
    return render(request, 'chat/index.html', {'chatrooms':chatrooms})

@login_required
def chatroom(request, slug):
    room = ChatRoom.objects.get(slug=slug)
    messages = ChatMessage.objects.filter(room=room)
    return render(request, 'chat/room.html', {'room':room, 'messages':messages})