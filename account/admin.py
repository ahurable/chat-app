from django.contrib import admin
from django.contrib.admin.decorators import register

from .models import CustomUser
# Register your models here.

@admin.register(CustomUser)
class AdminCustomUser(admin.ModelAdmin):

    list_display = ['email', 'phone_number', 'is_active', 'is_admin']
    