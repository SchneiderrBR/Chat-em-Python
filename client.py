from socket import *
from threading import Thread
import json
from protocol import Ptc

ipv4 = 'localhost'
ipv6 = '::1'
porta = 12001

info = getaddrinfo('localhost', None)[0]
if info[0] == AF_INET:  # IPv4
    clientSocket = socket(AF_INET)
    clientSocket.connect((ipv4, porta))
else:
    clientSocket = socket(AF_INET6)
    clientSocket.connect((ipv6, porta))

rec = clientSocket.recv(1024).decode()
recvMsg = json.loads(rec)
print(recvMsg['message'])


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
        recvMsg = json.loads(clientSocket.recv(1024).decode())
        if 'name' not in recvMsg:  # servidor
            print('>>>> : ' + recvMsg["message"])
        elif recvMsg["target"] == "§§":
            print("> " + recvMsg["name"] + ': ' + recvMsg["message"])
        else:
            print(recvMsg["target"] + " >> " + recvMsg["name"] + ': ' + recvMsg["message"])


login()
Thread(target=receive).start()

try:
    while True:
        sendMsg = input()
        if sendMsg.startswith("/"):
            if sendMsg.startswith('/join:'):
                if len(sendMsg.split(':')) == 2:
                    clientSocket.send(Ptc.join(sendMsg.split(':')[1]))
                elif len(sendMsg.split(':')) == 3:
                    clientSocket.send(Ptc.join(sendMsg.split(':')[1], None, sendMsg.split(':')[2]))
                else:
                    print('/help:join')
            elif sendMsg.startswith('/exit:'):
                if len(sendMsg.split(':')) == 2:
                    clientSocket.send(Ptc.part(sendMsg.split(':')[1]))
                else:
                    print('/help:exit')
            elif sendMsg.startswith('/help:'):
                if len(sendMsg.split(':')) == 2:
                    help(sendMsg.split(':')[1])
                else:
                    help()
            else:
                print("commando nao reconhecido, digite /help")
        elif sendMsg.startswith("*:"):
            clientSocket.send(Ptc.message('*', sendMsg.split(':')[1]))
        elif sendMsg.startswith("&:"):
            clientSocket.send(Ptc.message('&', sendMsg.split(':')[1]))
        elif sendMsg.startswith("#"):
            if len(sendMsg.split(':')) == 2:
                clientSocket.send(Ptc.message(sendMsg.split(':')[0], sendMsg.split(':')[1]))
            else:
                print('/help:message')
        elif len(sendMsg.split(':')) == 2:
            clientSocket.send(Ptc.message(sendMsg.split(':')[0], sendMsg.split(':')[1]))
        else:
            print("commando nao reconhecido, digite /help")
except:
    clientSocket.send(Ptc.disconnect())


def help(cmd=None):
    if cmd == "join":
        print("/join:name         =>  Entra no canal 'name'")
        print("/join:name:pass    =>  Entra no canal 'name' com a senha 'pass'")
        print("*Caso o canal nao exista, ele sera criado, e voce sera o admin")
        print("*Para saber mais sobre admin, digite /help:admin")
    elif cmd == "exit":
        print("/exit:name         =>  Sai do canal 'name'")
    elif cmd == "message":
        print("user:message       =>  Envia a mensagem 'message' para 'user'")
        print("#channel:message   =>  Envia a mensagem 'message' para o canal 'channel'")
        print("&:message          =>  Envia a mensagem 'message' para todos usuarios do servidor")
        print("*:message          =>  Envia a mensagem 'message' para todos os servidores")
    elif cmd == "admin":
        print("/admin:name        =>  Torna 'name' um admin do canal")
        print("*O primeiro admin sera quem criar o canal")
        print("*A unica permissao de admin é usar o comando /kick")
    elif cmd == "kick":
        print("/kick:name:channel =>  Expulsa 'name' do canal 'channel'")
        print("*Somente um admin pode usar esse comando")
    else:
        print("   - /help:message")
        print("   - /help:join")
        print("   - /help:exit")
        print("   - /help:admin")
