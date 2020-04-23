from socket import *
from threading import Thread
import json
import time
from protocol import Ptc

ipv4 = '0.0.0.0'
ipv6 = '::'
porta = 12001

socketList = []
users = {}
channels = {}
channelsPasw = {}


def setupIpv4():
    serverSocket = socket(AF_INET, SOCK_STREAM)
    serverSocket.bind((ipv4, porta))
    serverSocket.listen()
    socketList.append(serverSocket)
    while True:
        sock, addr = serverSocket.accept()
        socketList.append(sock)
        sock.send(Ptc.message('', 'conectado em: '+ipv4+':'+str(porta)))
        Thread(target=client, args=([sock])).start()


def setupIpv6():
    serverSocket = socket(AF_INET6, SOCK_STREAM)
    serverSocket.bind((ipv6, porta))
    serverSocket.listen()
    socketList.append(serverSocket)
    while True:
        sock, addr = serverSocket.accept()
        socketList.append(sock)
        sock.send(Ptc.message('', 'conectado em: '+ipv6+':'+str(porta)))
        Thread(target=client, args=([sock])).start()


def client(sock):
    while True:
        try:
            data = json.loads(sock.recv(2048).decode())
            if data["op"] == "MESSAGE":
                if data["target"] == "&":
                    for u in users:
                        users[u].send(Ptc.message('&', data["message"], 'user'))
                if data["target"][:1] == "#":
                    for c in channels:
                        if c == data["target"][1:]:
                            for u in channels[c]:
                                if u.startswith("§§"):
                                    u = u[2:]
                                users[u].send(Ptc.message(data["target"], data["message"], 'user'))
                        break
                else:
                    users[data["target"]].send(Ptc.message('§§', data["message"], 'user'))
            elif data["op"] == "LOGIN":
                if data["name"].lower() in users:
                    sock.send(Ptc.error('username already exist'))
                else:
                    users[data["name"].lower()] = sock
                    print("User " + data["name"] + " added.")
                    sock.send(Ptc.login(data["name"].lower()))
            elif data["op"] == "DISCONNECT":
                for u in users:
                    if users[u] == sock:
                        print(u + " foi desconectado")
                        users.remove(u)
                        break
            elif data["op"] == "JOIN":
                for u in users:
                    if users[u] == sock:
                        if data["channel"] not in channels:
                            if "pass" not in data:
                                channels[data["channel"]] = ["§§" + u]
                                channelsPasw[data["channel"]] = "§§"
                                sock.send(Ptc.message("","Voce criou o canal: "+ data["channel"]))
                            else:
                                channelsPasw[data["channel"]] = data["pass"]
                                channels[data["channel"]] = ["§§" + u]
                                sock.send(Ptc.message("","Voce criou o canal: "+ data["channel"]+" com a senha: "+ data["pass"]))
                        else:
                            if channelsPasw[data["channel"]] == '§§':
                                channels[data["channel"]].append(u)
                                sock.send(Ptc.message("","Voce entrou no canal: "+ data["channel"]))
                                ##avisar outor users no canal
                            else:
                                if("pass" not in data):
                                    sock.send(Ptc.message("","Este canal possui senha!"))
                                else:
                                    if data["pass"] == channelsPasw[data["channel"]]:
                                        channels[data["channel"]].append(u)
                                        sock.send(Ptc.message("","Voce entrou no canal: "+ data["channel"]))
                                    else: sock.send(Ptc.message("","Senha Incorreta!"))
                        #break
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
