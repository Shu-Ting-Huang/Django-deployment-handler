import os
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    return HttpResponse("Hello, world!! \n<br>The external IP is " + os.environ['EXTERNAL_IP'])