import socket


def start_server():
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 2000))
    server.listen(1)
    backsend, addr = server.accept()

    while True:
        data = backsend.recv(1024)
        if not data:
            break

    server.close()
