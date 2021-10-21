from django.urls import path

from .views import LoginView, RegisterView

app_name = "account"

urlpatterns = [
    path('register/', RegisterView.as_view(), name="register_url"),
    path('login/', LoginView.as_view(), name="login_url")
]
