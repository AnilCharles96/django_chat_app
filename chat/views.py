from django.shortcuts import render
from django.utils.safestring import mark_safe
import json
from django.contrib.auth.decorators import login_required
from django.views.generic.edit import CreateView
from .models import Message, Chat


# Create your views here.
@login_required(login_url='/login/')
def index(request):
    return render(request, 'chat/index.html', {})

@login_required(login_url='/login/')
def room(request, room_name):
    author = []
    content = []
        
    try:
        chat_obj = Chat.objects.get(name=room_name)
    except: 
        chat_obj = Chat.objects.create(name=room_name)
        chat_obj.save()

    message_obj = Message.objects.filter(chat_room=chat_obj)
 
    for values in message_obj:
        content.append(values.content)
        author.append(values.author)

    return render(request, 'chat/room.html', {
        'room_name_json': mark_safe(json.dumps(room_name)),
        'content_and_author': zip(content,author),
        'username': request.user
    })

