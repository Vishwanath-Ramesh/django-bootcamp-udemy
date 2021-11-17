from django.shortcuts import render
from django.http import HttpResponse

from app_1.models import User

def index(request):
    return HttpResponse('Welcome to Project 2')

def help(request):
    myContext = { } 
    return render(request, 'app_1/help.html', context=myContext)

def users(request):
    users = User.objects.order_by('first_name', 'last_name')
    myContext = { 'users': users }
    return render(request, 'app_1/users.html', context=myContext)