from django.shortcuts import render
from django.contrib.auth import get_user_model


User = get_user_model()


def index(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'index.html', context={
        'users': users,
    })


def chatPage(request):
    users = User.objects.exclude(username=request.user.username)
    return render(request, 'main_chat.html', context={
        'users': users,
    })
