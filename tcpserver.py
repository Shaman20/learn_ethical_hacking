from http import client
import socket
import threading

bind_ip = '0.0.0.0'
bind_port = 9999

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server.bind((bind_ip, bind_port))
server.listen(5)

print(f'Listening on {bind_port, bind_ip}')

def handle_client(clientSocket):
    request = clientSocket.recv(1024)
    
    print(f'Recieved {request}')
    
    clientSocket.send('ACK!!')
    clientSocket.close()
    
    
while True:
    client, addr = server.accept()
    print(f'Accepted connection from {addr[0], addr[1]}')
    
    client_handler = threading.Thread(target=handle_client, args=(client,))
    client_handler.start()