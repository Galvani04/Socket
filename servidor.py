import socket

# gera o socket
# AF_INET == ipv4
# SOCK_STREAM == TCP

HOST = ''
PORT = 50000

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # Gera um socket ipv4 com protocolo tcp
s.bind((socket.gethostname(), PORT)) # Se vincula a um host name e port
s.listen(1) # Gera uma quantidade x de posiveis conexões com o servidor

print('Aguardando conexão')
(conn, ender) = s.accept() # Aguarda a requisição do cliente

print(f'conectado em {ender}') # Formata a string e mostra quem se conectou
while True:
    # Gera um buffer de 1024 bytes e espera mensagem
    data = conn.recv(1024)

    # Transforma os dados recebidos de bytes para utf-8
    msg = data.decode("utf-8")                              
    
    # Se a mensagem for "fechar" encerra a conexao
    if "fechar" == msg:
        print('Fechando a conexão')
        # Pede para o cliente encerrar a conexao
        conn.sendall(bytes('',"utf-8"))
        break # Finaliza o loop
    else:
        print(msg) # printa a mensagem enviada pelo cliente
        data = input() # Libera a entrada de dados no console
        conn.sendall(bytes(data,"utf-8")) # Envia o dado digitado pelo cliente

# Encerra a conexao do lado servidor
conn.close()