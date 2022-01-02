import os
import urllib.request

external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
port = '1234'

if os.name == 'nt': # Windows
    python_cmd = 'python'
elif os.name == 'posix': # Linux
    python_cmd = 'python3'
os.system(python_cmd + ' manage.py runserver --insecure' + external_ip + ':' + port)