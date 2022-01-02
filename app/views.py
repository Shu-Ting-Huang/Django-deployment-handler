import os
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    if os.name == 'posix':
        # pull from GitHub
        root_folder_path = os.environ['ROOT_FOLDER_PATH']
        os.chdir(root_folder_path)
        os.system('git fetch --all')
        os.system('git reset --hard origin/master')

        # Set DEBUG = False and ALLOWED_HOSTS = ['*'] in settings.py
        settings_location = os.environ['SETTINGS_PATH']
        new_content = ""
        with open(settings_location, 'r') as f:
            for line in f:
                if line.startswith("DEBUG"):
                    new_content += "DEBUG = False\n"
                elif line.startswith("ALLOWED_HOSTS"):
                    new_content += "ALLOWED_HOSTS = ['*']\n"
                else:
                    new_content += line
        with open(settings_location, 'w') as f:
            f.write(new_content)

    return HttpResponse("Hello, world!! " + os.environ['SETTINGS_PATH'])