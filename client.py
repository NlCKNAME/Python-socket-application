import socket

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket

Socket.connect(('127.0.0.1', 63000))

print("Connexion OK !")

Socket.send(b'Status Server ?')

message = Socket.recv(1024)

print(str(message.decode()))

Socket.close()