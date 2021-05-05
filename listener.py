# Setting up server to listen to incoming connections instead of using netcat

import socket

listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
listener.bind(("192.168.1.38", 4444))
listener.listen(0)  # specifying a backlog
print("[+] Waiting for connection")
listener.accept()
print("[+] Got a connection")

