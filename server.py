from socket import *
from threading import Thread
import json
import time
from protocol import Ptc

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
        sock.send(Ptc.message('', '"conectado em: IPV4:12000"'))
        Thread(target=client, args=([sock])).start()


def setupIpv6():
    serverSocket = socket(AF_INET6, SOCK_STREAM)
    serverSocket.bind((ipv6, porta))
    serverSocket.listen()
    socketList.append(serverSocket)
    while True:
        sock, addr = serverSocket.accept()
        socketList.append(sock)
        sock.send(Ptc.message('', 'conectado em: IPV6:12000'))
        Thread(target=client, args=([sock])).start()


def client(sock):
    while True:
        try:
            data = json.loads(sock.recv(2048).decode())
            if data["op"] == "LOGIN":
                if data["name"].lower() in users:
                    sock.send(Ptc.error('username already exist'))
                else:
                    users[data["name"].lower()] = sock
                    print("User " + data["name"] + " added.")
                    sock.send(Ptc.login(data["name"].lower()))

            elif data["target"] == "&":
                for u in users:
                    users[u].send(Ptc.message('&', data["message"], 'user'))
            else:
                users[data["target"]].send(Ptc.message('§@', data["message"], 'user'))
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
