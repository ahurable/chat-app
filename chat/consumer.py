from channels.generic.websocket import WebsocketConsumer
import json

from .models import RoomMessageModel

class ChatHandler(WebsocketConsumer):

  def connect(self):
      self.user = self.scope['user']

      self.roomname = self.scope['path'].split('/')[2]

      self.room_model = RoomMessageModel.objects.get(name=self.roomname)
      self.messages = self.room_model.message["message"]
      print(self.messages)

      self.accept()

      for message in self.messages:
          self.send(text_data=json.dumps(message))

  def disconnect(self, code):
      return super().disconnect(code)

  def receive(self, text_data=None, bytes_data=None):

      data = json.loads(text_data)
    #   roomname = self.scope['path'].split('/')[2]

    #   room_model = RoomMessageModel.objects.get(name=roomname)
    #   messages = room_model.message["message"]
    #   print(messages)
      message = data['message']
      user = self.scope['user']
      if user.is_authenticated:
          username = user.username
          new_message = {'username':str(username), 'message':str(message)}
          self.room_model.message['message'].append(new_message)
          self.room_model.save()
          self.send(text_data=json.dumps(new_message))
      else:
          self.send(text_data=json.dumps({'username':'Site Says: ', 'message': 'You should to authenticate first'}))   
      