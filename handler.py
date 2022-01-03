import os
import urllib.request
from urllib.parse import urlparse, parse_qs
from http.server import HTTPServer, BaseHTTPRequestHandler

external_ip = urllib.request.urlopen('https://api.ipify.org').read().decode('utf8')
port = 1234
root_folder_path = "/test-project"
remote_name = "origin"

class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        # get path from url, expected to be "/update"
        path = urlparse(self.path).path

        # get params from url, expected be {"branch": <branch pushed to GitHub>}
        params = {k:v[0] for k,v in parse_qs(urlparse(self.path).query).items()}

        if path == '/update' and list(params.keys()) == ['branch']:
            # pull the newly update branch from GitHub
            pushed_branch = params['branch']
            os.chdir(root_folder_path)
            checked_out_branch = os.popen('git branch --show-current').readlines()[0].strip('\n')
            os.system('git fetch ' + remote_name + ' ' + pushed_branch)
            if checked_out_branch == pushed_branch:
                os.system('git reset --hard ' + remote_name + '/' + pushed_branch)
            else:
                os.system('git branch --force ' + pushed_branch + ' ' + remote_name + '/' + pushed_branch)

            # load and resave manage.py to force the server to reload
            with open('manage.py', 'r') as f:
                manage_py = f.read()
            with open('manage.py', 'w') as f:
                f.write(manage_py)

            # send response
            self.send_response(200)
            self.send_header('Content-type', 'text/html')
            self.end_headers()
            self.wfile.write(bytes('<h1>Successfully pulled branch ' + pushed_branch + ' from GitHub' + ' </h1>','utf-8'))

server = HTTPServer((external_ip, port), MyHandler)
print('Server started on ' + external_ip + ':' + str(port))
server.serve_forever()
print('Server stopped')