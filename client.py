import socket
import time

HOST = 'localhost'
PORT = 3000

s = socket.socket()
s.connect((HOST, PORT))

while True:
    # Recebe
    data = s.recv(1024) # Numero de bytes que ele vai trazer

    print(data.decode('utf-8'))
    time.sleep(2)