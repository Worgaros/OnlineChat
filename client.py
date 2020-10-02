import socket
import threading

HOST = '127.0.0.1'
PORT = 6666

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect((HOST, PORT))

#receive message from the server and print it in the console
def ReceiveMessages(client, addr):
    while True:
        data = client.recv(1024).decode()
        print(data)

#start multithreading to receive messages and write message in same time
while True:
    threading._start_new_thread(ReceiveMessages, (client, ''))
    data = input()
    client.sendall(data.encode())