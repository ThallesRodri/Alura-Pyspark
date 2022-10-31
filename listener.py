import socket
import time

HOST = 'localhost'
PORT = 3000

s = socket.socket()
s.bind((HOST, PORT)) # Bind associa o socket a porta e ao host
print(f'Aguardando conexão na porta: {PORT}')

# Coloca o socket em operação. Aguarda a solicitação do cliente para se comunicar.
s.listen(5) # O parametro significa que ele deixa 5 conexoes enfileiradas esperando para serem usadas  
conn, address = s.accept() # Aceita a conexão do cliente

print(f'Recebendo solicitação de {address}')

messages = {
    'Mensagem A',
    'Mensagem B',
    'Mensagem C',
    'Mensagem D',
    'Mensagem E',
    'Mensagem F',
    'Mensagem G'
}

for message in messages:
    message = bytes(message, 'utf-8')
    conn.send(message)
    time.sleep(5)

conn.close()