#!/usr/bin/env python

import socket

connection = socket.socket(socket.AF_INET , socket.SOCK_STREAM)
connection.connect(("192.168.1.38", 4444))

connection.send("\n[+] Connection established.\n".encode())


recieved_data = connection.recv(1024)
print(recieved_data)






connection.close()

