import os
import json

# Get server IP from user
server_ip = input("Enter the server IP: ")

# change to the directory in which THIS SCRIPT is located
os.chdir(os.path.dirname(os.path.abspath(__file__)))

# update the server IP in server_info.json
with open("server_info.json", "r") as f:
    server_info = json.load(f)
server_info["server_ip"] = server_ip
with open("server_info.json", "w") as f:
    f.write(json.dumps(server_info, indent = 4))