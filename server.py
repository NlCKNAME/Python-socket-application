import socket

port = 63000

Socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #Create socket

Socket.bind(('', port))

print("Serveur en écoute ...")
Socket.listen()

conn_client, addr_client = Socket.accept()
print("Nouvelle connexion client : " + str(addr_client))

message = conn_client.recv(1024)

print("Donnée reçu : " + str(message.decode()))

conn_client.send(message + b'\nServer OK')

conn_client.close()

Socket.close()