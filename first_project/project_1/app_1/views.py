from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
    # return HttpResponse('Hello world!!') # simple text response
    myContext = { 'userName': 'Vishwanath' }
    return render(request, 'app_1/index.html', context=myContext)