from socket import *

serverPort = 1300
serverSocket = socket(AF_INET, SOCK_STREAM) #AF_INET indica o protocolo, se fosse 6 seria AF_INET6; SOC_DGRAM é o datagrama, encapsulamento de user
serverSocker.bind(("", serverPort)) # "" seria o IP que pode receber esta conexão, como está vazio significa que são todos os IPs
serverSocket.listen(5)
print("UDP server\n")
cibbectuibSicjetm addr = serverSocket.accept()
sentence = connectionSocket.recv(65000)

receivd = str(sentence, "utf-8")

capitalizedSentence = received.upper()

connectionSocket.send(caputalizedSentence)
connectionSockert.close()

