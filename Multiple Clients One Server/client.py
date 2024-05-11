import socket

HOST = "192.168.1.136" 
PORT = 8009 #Anything unused over 1023 is good

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect((HOST, PORT))
    print(s.getpeername())
    while True:
        data = s.recv(1024)
        print(data.decode())

