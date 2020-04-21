from socket import *
from threading import Thread

socketList = []
users = {}
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost', 12000))
serverSocket.listen()
socketList.append(serverSocket)

def client(sock):
    while True:
        try:
            data = sock.recv(2048).decode()
            if data.startswith("¥"):
                users[data[1:].lower()] = sock
                print("User " + data[1:] + " added.")
                sock.send(("Seu user é: " + str(data[1:])).encode())
            elif data.find("§@:") != -1:
                for u in users:
                    user = data.split("§")[1]
                    msg = data.split("§")[2].split(":")[1]
                    users[u].send((user + ": " + msg).encode())
            elif data.startswith("§"):
                user = data.split("§")[1]
                msg = data.split("§")[2].split(":")[1]
                dest = data.split("§")[2].split(":")[0]
                users[dest].send((user + ": " + msg).encode())
        except:
            continue

while True:
    sock, addr = serverSocket.accept()
    socketList.append(sock)
    sock.send(("conectado em: " + str(addr)).encode())
    Thread(target=client, args=([sock])).start()