from socket import *

serverName = "" #IP alvo, onde quero chegar
serverPort = 12500
serverSocket = socket(AF_INET, SOCK_DGRAM) #AF_INET indica o protocolo, se fosse 6 seria AF_INET6; SOC_DGRAM é o datagrama, encapsulamento de user
serverSocker.bind(("", serverPort)) # "" seria o IP que pode receber esta conexão, como está vazio significa que são todos os IPs

print("UDP Client\n")

while 1:
    message = input("Input message: ")
    if message =="exit":
        break
    clientSocket.sendto(bytes(message, "utf-8"), (serverName, serverPort))
    clientSocket.close()
