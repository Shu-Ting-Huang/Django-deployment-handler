# Django Deployment Handler
Put the following configurations in `settings.py`:
```
import os
if os.name == 'posix':
    DEBUG = False
else:
    DEBUG = True
ALLOWED_HOSTS = ['*']
```
Run the following commands in local Django project repository:

`> git submodule add https://github.com/Shu-Ting-Huang/Django-deployment-handler.git`

`> python Django-deployment-handler/set_server_ip.py`

`> git add .`

`> git commit -m "Add deployment handler as submodule and set up server IP"`

`> git push origin master`

Run the following commands on the server:

`$ git clone --recurse-submodules (Django repo URL)`

`$ cd (Django repo name)`

`$ python3 Django-deployment-handler/runserver.py`
