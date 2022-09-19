import socket

HOST = "127.0.0.1"
PORT = 8008

kb_recv = 0
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected at IP address and port {addr}")
        with open('test.out', 'wb') as f:
            while True:
                data = conn.recv(1024)
                if not data:
                    break
                else:
                    f.write(data)
                    kb_recv += 1

print(f"Server received {kb_recv} kb of data.")