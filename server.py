import socket
import threading

HOST = '127.0.0.1'
PORT = 6666
CLIENTS = []

#check which client sen a message and send it to the other
def ReceiveMessages(client, addr):
    while True:
        data = client.recv(1024).decode()
        if client == CLIENTS[0]:
            data1 = data
            CLIENTS[1].sendall(data1.encode())
        elif client == CLIENTS[1]:
            data2 = data
            CLIENTS[0].sendall(data2.encode())

server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind((HOST, PORT))
server.listen(2)

#start multithreading for max 2 clients and call the function to receive messages from clients
while True:
    if len(CLIENTS) < 2:
        conn, addr = server.accept()
        CLIENTS.append(conn)
        threading._start_new_thread(ReceiveMessages, (conn, addr))
        print("Connected to:", addr)