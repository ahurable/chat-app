from django.core.exceptions import ValidationError
from django.db import models
from django.contrib.auth.models import AbstractBaseUser, BaseUserManager

import os
# Create your models here.


def img_path(instance, file):
    
    name, ext = os.path.splitext(file)
    path = f'avatars/{instance.username}{ext}'
    return path



class CustomUserManager(BaseUserManager):

    def create_user(self, email, phone_number, password=None):
        
        if not email: 
            raise ValueError('User email must be set!')

        user = self.model(
            email = email,
            phone_number = phone_number
        )
        user.set_password(password)
        user.save(using=self._db)

        return user


    def create_superuser(self, email, phone_number, password=None):

        user = self.create_user(
            email=email,
            phone_number=phone_number,
            password=password
        )

        user.is_admin = True

        user.save(using=self._db)
        return user



class CustomUser(AbstractBaseUser):

    email = models.EmailField(
        verbose_name="email",
        max_length=55,
        unique=True
    )
    phone_number = models.DecimalField(
        decimal_places=1,
        max_digits=12
    )
    joined_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ('phone_number', )
    objects = CustomUserManager()

    def __str__(self):
        return str(self.email)

    def has_perm(self, perm, obj=None):
        return True

    def has_module_perms(self, app_label):
        return True

    @property
    def is_staff(self):
        return self.is_admin


class ProfileModel(models.Model):

    user = models.OneToOneField(
        CustomUser,
        related_name='profile_model',
        on_delete=models.CASCADE
    )
    username = models.CharField(
        max_length=16,
        unique=True,
        blank=True,
        null=True
    )
    biography = models.TextField()
    profile_picture = models.ImageField(
        upload_to=img_path,
        default='/media/image/avatar.png'
    )

    def __str__(self):
        return str(self.username)