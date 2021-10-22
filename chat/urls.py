from django.urls import path

from .views import GetUsernameDirect

app_name="chat"

urlpatterns = [
    path('direct/<str:chatroom>', GetUsernameDirect, name="direct_url")
]
