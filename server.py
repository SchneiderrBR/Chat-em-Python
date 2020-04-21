from socket import *
import select

socketList = []
users = {}
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('localhost',12000))
serverSocket.listen()
socketList.append(serverSocket)

while True:
    ready_to_read,ready_to_write,in_error = select.select(socketList,[],[],0)
    for sock in ready_to_read:
        if sock == serverSocket:
            connect, addr = serverSocket.accept()
            socketList.append(connect)
            connect.send(("conectado em: " + str(addr)).encode())
        else:
            try:
                data = sock.recv(2048).decode()
                if data.startswith("¥"):
                    users[data[1:].lower()] = connect
                    print("User " + data[1:] +" added.")
                    connect.send(("Seu user é: "+str(data[1:])).encode())
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