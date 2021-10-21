from channels.generic.websocket import WebsocketConsumer
import json

class ChatHandler(WebsocketConsumer):

  def connect(self):
      self.user = self.scope['user']
      self.accept()

  def disconnect(self, code):
      return super().disconnect(code)

  def receive(self, text_data=None, bytes_data=None):

      data = json.loads(text_data)
      message = data['message']
      user = self.scope['user']
      if user.is_authenticated:
          email = user.email
          print(str(email))

      self.send(text_data=json.dumps({'email':str(email), 'message':message}))