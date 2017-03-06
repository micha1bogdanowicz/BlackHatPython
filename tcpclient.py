#!/usr/bin/python

import socket

host="127.0.0.1"
PORT=9999
client = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

client.connect((host,PORT))

#client.send("GET / HTTP/1.1\r\nHost: google.com\r\n\r\n")
client.send("ABCSASDSA")
data=client.recv(4096)
print data
client.close()