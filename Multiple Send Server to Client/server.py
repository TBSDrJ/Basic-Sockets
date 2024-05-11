import socket
import time

HOST = ""
PORT = 8009

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        while True:
            data = "Hello client!".encode()
            conn.sendall(data)
            print("Server message sent.")
            time.sleep(3)
            