from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(request):
    myContext = { } 
    return render(request, 'app_1/help.html', context=myContext)