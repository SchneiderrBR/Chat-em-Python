from socket import *
from threading import Thread
import json
import time

ipv4 = '0.0.0.0'
ipv6 = '::'
porta = 12000

socketList = []
users = {}


def setupIpv4():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((ipv4, porta))
    serverSocket.listen()
    socketList.append(serverSocket)
    while True:
        sock, addr = serverSocket.accept()
        socketList.append(sock)
        sock.send("conectado em: IPV4:12000".encode())
        Thread(target=client, args=([sock])).start()


def setupIpv6():
    serverSocket = socket(AF_INET6, SOCK_STREAM)
    serverSocket.bind((ipv6, porta))
    serverSocket.listen()
    socketList.append(serverSocket)
    while True:
        sock, addr = serverSocket.accept()
        socketList.append(sock)
        sock.send("conectado em: IPV6:12000".encode())
        Thread(target=client, args=([sock])).start()


def client(sock):
    while True:
        try:
            data = sock.recv(2048).decode()
            if data.startswith("¥"):

                if data[1:].lower() in users:
                    sock.send("0".encode())
                else:
                    users[data[1:].lower()] = sock
                    print("User " + data[1:] + " added.")
                    sock.send("1".encode())

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


Thread(target=setupIpv4).start()
Thread(target=setupIpv6).start()
print("Servidor iniciado")

while True:
    cmd = input()
    ##desligar servidor
    ##enviar mensagem pra 1 user
    ##enviar mensagem pra @
    time.sleep(10)
