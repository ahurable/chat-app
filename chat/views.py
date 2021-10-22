from django.http.response import HttpResponse
from django.shortcuts import render, redirect

from .models import RoomMessageModel
# Create your views here.

def GetUsernameDirect(request, chatroom):

  if not request.user.is_authenticated:
     return redirect('account:register_url')

  if not RoomMessageModel.objects.filter(name=chatroom).exists():
     return HttpResponse("This chatroom does not exist")
  
  context = {
    'chatroom':chatroom,
  }
  return render(request, 'direct.html', context)