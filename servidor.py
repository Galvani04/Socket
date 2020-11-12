import socket

# gera o socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

HOST = ''
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((socket.gethostname(), PORT))
s.listen(1)

print('Aguardando conexão')
(conn, ender) = s.accept()

print(f'conectado em {ender}')
while True:
    data = conn.recv(1024)
    msg = data.decode("utf-8")
    
    if "fechar" == msg:
        print('Fechando a conexão')
        conn.sendall(bytes('',"utf-8"))
        break
    else:
        print(msg)
        data = input()
        conn.sendall(bytes(data,"utf-8"))

conn.close()