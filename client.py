from socket import *
from threading import Thread

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

recvMsg = clientSocket.recv(1024)
print(recvMsg.decode())  # confirmação de conexão

user = input("Digite seu Username:")
sendMsg = '¥' + user
clientSocket.send(sendMsg.encode())


def receive():
    while True:
        recvMsg = clientSocket.recv(1024)
        print("> " + recvMsg.decode())


Thread(target=receive).start()

# print("[User:Mensagem]")
while True:
    sendMsg = input()
    sendMsg = '§' + user + '§' + sendMsg
    clientSocket.send(sendMsg.encode())
