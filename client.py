import socket

HOST = "127.0.0.1" #localhost
PORT = "8008" #Anything unused over 1023 is good

kb_sent = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.connect(HOST, PORT)
    with open('test.data', 'rb') as f:
        while True:
            data = f.read(1024)
            if data:
                s.sendall(data)
                kb_sent += 1
            else:
                break
print(f"Socket closed. Send {kb_sent}kb of data.")