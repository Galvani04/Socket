import socket

# gera o socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

HOST = '127.0.0.1'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((socket.gethostname(), PORT))

while True:
    data = input()
    s.sendall(bytes(data,"utf-8"))
    data = s.recv(1024)
    msg = data.decode("utf-8")

    if (msg == "fechar") or (not data):
        s.sendall(bytes("fechar","utf-8"))
        break
    else:
        print(msg)

print('Fechando a conexão!')
s.close()