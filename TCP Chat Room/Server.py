
import socket
import threading

# Server settings
host = '127.0.0.1'
port = 55555

# Create socket and bind it
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((host, port))
server.listen()

clients = []
nicknames = []

# Send message to all clients
def broadcast(message):
    for client in clients:
        client.send(message)

# Handle messages from a client
def handle(client):
    while True:
        try:
            message = client.recv(1024)
            broadcast(message)
        except:
            index = clients.index(client)
            clients.remove(client)
            client.close()
            nickname = nicknames[index]
            broadcast(f"{nickname} has left the chat!".encode('utf-8'))
            nicknames.remove(nickname)
            break

# Receive new connections
def receive():
    print("Server is running and listening for connections...")
    while True:
        client, address = server.accept()
        print(f"New connection from {str(address)}")

        client.send("NICKNAME".encode('utf-8'))
        nickname = client.recv(1024).decode('utf-8')
        nicknames.append(nickname)
        clients.append(client)

        print(f"Nickname is {nickname}")
        broadcast(f"{nickname} joined the chat!".encode('utf-8'))
        client.send("You are now connected to the server!".encode('utf-8'))

        thread = threading.Thread(target=handle, args=(client,))
        thread.start()

receive()
