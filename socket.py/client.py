import socket 

cliente = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

cliente.connect('localhost', 8888)

terminado = False   
print('digite tt para terminar o chat')

while not terminado:
    cliente.sec(input('Mensagem: '.encode('utf-8')) )
                
