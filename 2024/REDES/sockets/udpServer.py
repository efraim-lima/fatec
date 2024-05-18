from socket import *

serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM) #AF_INET indica o protocolo, se fosse 6 seria AF_INET6; SOC_DGRAM é o datagrama, encapsulamento de user
serverSocker.bind(("", serverPort)) # "" seria o IP que pode receber esta conexão, como está vazio significa que são todos os IPs

print("UDP server\n")

while 1:
    message, clientAddress = sererSocket.recvfrom(2048) #2048 é o limite de bytes
    text = str(message
