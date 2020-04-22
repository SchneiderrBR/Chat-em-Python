from socket import *
from threading import Thread
import json
from protocol import Ptc

ipv4 = 'localhost'
ipv6 = '::1'
porta = 12000

info = getaddrinfo('localhost', None)[0]
if info[0] == AF_INET:  # IPv4
    clientSocket = socket(AF_INET)
    clientSocket.connect((ipv4, porta))
else:
    clientSocket = socket(AF_INET6)
    clientSocket.connect((ipv6, porta))

rec = clientSocket.recv(1024).decode()
recvMsg = json.loads(rec)
print(recvMsg['message'])  # confirmação de conexão


def login():
    global user
    user = input("Digite seu Username:")
    clientSocket.send(Ptc.login(user))
    if json.loads(clientSocket.recv(1024).decode())["op"] == 'LOGIN':
        print("Seu user é: " + user.lower())
    else:
        print("Nome de usuario nao disponivel")
        login()


def receive():
    while True:
        # print(clientSocket.recv(1024).decode())
        recvMsg = json.loads(clientSocket.recv(1024).decode())
        if recvMsg["name"] == None:  # servidor
            print('>>>> : ' + recvMsg["message"])
        if recvMsg["target"] == "§@":
            print("> " + recvMsg["name"] + ': ' + recvMsg["message"])
        else:
            print(recvMsg["target"] + " >> " + recvMsg["name"] + ': ' + recvMsg["message"])


login()
Thread(target=receive).start()

# print("[User:Mensagem]")
while True:
    sendMsg = input()
    if sendMsg.startswith("/"):
        # comandos
        continue
    elif sendMsg.startswith("*:"):
        clientSocket.send(Ptc.message('*', sendMsg.split(':')[1]))
    elif sendMsg.startswith("&:"):
        clientSocket.send(Ptc.message('&', sendMsg.split(':')[1]))
    elif sendMsg.find(':') != -1:
        clientSocket.send(Ptc.message(sendMsg.split(':')[0], sendMsg.split(':')[1]))
    else:
        print("commando nao reconhecido")
