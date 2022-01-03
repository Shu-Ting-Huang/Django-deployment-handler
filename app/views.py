import os
from django.shortcuts import HttpResponse

# Create your views here.

def index(request):
    on_server = (os.name=='posix')
    if on_server:
        # pull from GitHub
        root_folder_path = os.environ['ROOT_FOLDER_PATH']
        remote_name = os.environ['REMOTE_NAME']
        pushed_branch = request.GET['branch']
        os.chdir(root_folder_path)
        checked_out_branch = os.popen('git branch --show-current').readlines()[0].strip('\n')
        os.system('git fetch ' + remote_name + ' ' + pushed_branch)
        if checked_out_branch == pushed_branch:
            os.system('git reset --hard ' + remote_name + '/' + pushed_branch)
        else:
            os.system('git branch --force ' + pushed_branch + ' ' + remote_name + '/' + pushed_branch)

    return HttpResponse("Hello, world!!")