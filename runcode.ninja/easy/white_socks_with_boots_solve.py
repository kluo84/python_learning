#!/usr/bin/env python
import sys
import socket

url = sys.argv[1]
port = sys.argv[2]

s =  socket.socket(socket.AF_INET, socket.SOCK_STREAM)
ip = socket.gethostbyname(url)
s.connect((ip, int(port)))
print s.recv(1024)
s.close()
