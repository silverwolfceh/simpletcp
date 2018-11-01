import socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server_address = ('updatesrv.herokuapp.com', 12345)
sock.connect(server_address)
while True:
    data = sock.recv(1024)
    print(data)