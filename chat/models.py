from django.db import models
from account.models import CustomUser
from jsonfield import JSONField

class RoomMessageModel(models.Model):

  creator = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
  name = models.CharField(max_length=200, unique=True, null=True)
  message = JSONField(default={"message":[]})

  def __str__(self) -> str:
    return str(self.name)