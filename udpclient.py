#!/usr/bin/python

import socket

host="127.0.0.1"
PORT=80


client = socket.socket(socket.AF_INET,socket.SOCK_DGRAM)


client.sendto("abcd",(host,PORT))

data,addr=client.recvfrom(4096)

print data