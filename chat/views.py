from django.shortcuts import render

# Create your views here.

def GetUsernameDirect(request, username):


  
  context = {
    'username':username,
  }
  return render(request, 'direct.html', context)