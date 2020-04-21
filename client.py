from socket import *
from threading import Thread

clientSocket = socket(AF_INET6)
clientSocket.connect(('localhost', 12000))
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
