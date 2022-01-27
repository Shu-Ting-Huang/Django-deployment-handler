import os
import json
from string import Template

default_deployment_port = 1234

# Get server IP from user
server_ip = input("Enter the server IP: ")

# change to the directory in which THIS SCRIPT is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# update the server IP in ../server_info.json
try:
    with open("../server_info.json", "r") as f:
        server_info = json.load(f)
        server_info["server_ip"] = server_ip
except FileNotFoundError:
    server_info = {"server_ip": server_ip, "deployment_port": default_deployment_port}
with open("../server_info.json", "w") as f:
    f.write(json.dumps(server_info, indent = 4))
del server_info

# set up GitHub actions script
os.makedirs("../.github/workflows", exist_ok = True) # create this directory if not exist
with open("../.github/workflows/deploy.yml", "w") as f:
    with open("../server_info.json", "r") as g:
        server_info = json.load(g)
    with open("template.yml", "r") as g:
        src = Template(g.read())
        f.write(src.substitute(server_info))