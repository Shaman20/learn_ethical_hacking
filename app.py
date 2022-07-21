from http import client
import socket
from urllib import response

target_host = 'www.google.com'
target_port = 80

# Socket Object
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the client
client.connect((target_host,target_port))

# Send some data
output = 'Thank you'
client.send(output.encode('utf-8'))

# Recieve some data
response = client.recv(4096)

print(response)