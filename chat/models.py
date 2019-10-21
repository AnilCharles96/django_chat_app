from django.db import models
from django.contrib.auth.models import User


class Chat(models.Model):
    name = models.CharField(primary_key=True,max_length=200)

    def __str__(self):
        return self.name


class Message(models.Model):
    chat_room = models.ForeignKey(Chat,on_delete=models.CASCADE,blank=True,null=True)
    author = models.ForeignKey(User,on_delete=models.CASCADE)
    content = models.CharField(max_length=200,blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.author.username

    def last_10_messages(self):
        return Message.objects.order_by('-timestamp').all()[:10]


    

    

