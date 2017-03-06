#!/usr/bin/python

import socket
import threading

host="0.0.0.0"
PORT=9999

def handle_client(client_socket):
    request = client_socket.recv(1024)
    print "[*] Odebrano: %s" % request
    client_socket.send("AFK!")
    client_socket.close()


server = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
server.bind((host,PORT))
server.listen(5)

print "[*] Nasluchiwanie na porcie %s:%d" % (host,PORT)


while True:
    client,addr=server.accept()
    client.send("abcd")
    print "[*] Przyjeto polaczenie od: %s:%d" % (addr[0],addr[1])
    client_handler= threading.Thread(target=handle_client,args=(client,))
    client_handler.start()
