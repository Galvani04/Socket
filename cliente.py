import socket

# gera o socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

HOST = '127.0.0.1'
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Gera um socket ipv4 com protocolo tcp
s.connect((socket.gethostname(), PORT)) # Se conecta ou host e a porta

# Mantem a interatividade ate que a conexao se encerre
while True:
    data = input() # Libera a entrada de dados no console
    s.sendall(bytes(data,"utf-8")) # Envia a mensagem para o servidor
    data = s.recv(1024) # Gera um buffer de 1024 bytes e espera mensagem
    msg = data.decode("utf-8") # Decodifica a mendagem para utf-8

    # Se receber "fechar" ou um dado vazio finaliza a conexao
    if (msg == "fechar") or (not data):
        # Pede para o servidor encerrar a conexao
        s.sendall(bytes("fechar","utf-8"))
        break # Finaliza o loop
    else:
        print(msg) # printa a mensagem enviada pelo servidor

print('Fechando a conexão!')
# Encerra a conexao do lado cliente
s.close()