from django.shortcuts import render
from django.http import HttpResponse

from app_1.models import Topic, Webpage, AccessRecord

# Create your views here.
def index(request):
    # return HttpResponse('Hello world!!') # simple text response
    # myContext = { 'userName': 'Vishwanath' }
    records = AccessRecord.objects.order_by('date')
    recordDates = { 'userName': 'Vishwanath', 'access_records': records }
    return render(request, 'app_1/index.html', context=recordDates)