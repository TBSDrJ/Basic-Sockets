import socket
import time

HOST = ""
PORT = 8009

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    clients = []
    client_ports = []
    while len(clients) < 2:
        conn, addr = s.accept()
        clients.append(conn)
        print(f"{len(clients)} clients attached.")
    with conn:
        while True:
            data = "Hello client!".encode()
            for conn in clients:
                conn.sendall(data)
            print("Server message sent.")
            time.sleep(3)
            