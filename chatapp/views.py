from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login
# Create your views here.
from django.http import HttpResponse
from django.template import loader
from .models import Group, User, Message

def login_view(request):
    if request.method == "POST":
        template = loader.get_template("login.html")
        username = request.POST.get('username')
        password = request.POST.get('password')
        groupkey = request.POST.get('group-key')
        # print(username)
        try:
            user = User.objects.get(username = username, password = password)
            group = Group.objects.get(groupkey = groupkey)
            groupname = group.groupname      
            username = user.username
            # Pass the group name to the session for use in the chat page
            request.session['group_name'] = groupname
            request.session['username'] = username
            return redirect('chat')  # Redirect to the chat pag
        except User.DoesNotExist:
                return HttpResponse("Invalid credentials. Please try again.")
        # print(User.objects.all().values())
    return render(request, 'login.html')
    # return HttpResponse(template.render(request))

def chat_view(request):
    groupname = request.session.get('group_name', 'School Forum Chat')
    username = request.session.get('username', 'School Forum Chat')
    print(username)
    user = User.objects.get(username = username)
    group = Group.objects.get(groupname = groupname)
    groupid = group.groupid
    messages = Message.objects.filter(messagegroup = groupid).values()
    context = {'group_name': groupname,
               'messages': messages}
    # print(messages)
    if request.method == "POST":
         newmessage = request.POST.get('newmessage')
         message = Message(messagecontent=newmessage, messagegroup = group, messagesender=user)
         message.save()
         return redirect('chat')

    return render(request, "chat.html", context)