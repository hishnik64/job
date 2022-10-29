import  socket

server = socket.socket()
server.connect(('localhost', 2000))
server.send('Hellow')

data = server.recv(1024)
server.close()

print(data)