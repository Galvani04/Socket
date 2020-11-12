import socket

# gera o socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

HOST = ''
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind((HOST, PORT))
s.listen()
print('Aguardando conexão')
conn, ender = s.accept()

print('conectado em', ender)
while True:
    data = conn.recv(1024)
    msg = data.decode("utf-8")
    print(msg)
    
    if "fechar" == msg:
        print('Fechando a conexão')
        break

    if data:
        data = input()
        conn.sendall(bytes(data,"utf-8"))

conn.close()