import socket
HOST = '127.0.0.1'
PORT = 50000
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((HOST, PORT))
while True:
    data = input()
    s.sendall(bytes(data,"utf-8"))
    data = s.recv(1024)
    
    if not data:
        print('Fechando a conexão!')
        break
    else:
        msg = data.decode("utf-8")
        print(msg)

s.close()