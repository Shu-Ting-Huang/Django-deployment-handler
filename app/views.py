import os
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    # pull from GitHub
    root_folder_path = os.environ['ROOT_FOLDER_PATH']

    # Set DEBUG = False and ALLOWED_HOSTS = ['*'] in settings.py
    settings_location = os.environ['SETTINGS_PATH']

    return HttpResponse("Hello, world!! " + os.environ['SETTINGS_PATH'])