import hashlib
import time

senha = "123"
tentativas = 0
bloqueado = False
bloqueio_tempo = 30

senha = hashlib.sha256(senha.encode()).hexdigest()

while tentativas < 3 and not bloqueado:
    senha_input = input("Digite a senha: ")
  
    if hashlib.sha256(senha_input.encode()).hexdigest() != senha:
        print("Senha incorreta. Tente novamente")
        tentativas += 1
        time.sleep(bloqueio_tempo)
        continue
    else:
        print("Senha correta, login efetivado!")
        break

if tentativas == 3 and not bloqueado:
    print("Você esgotou suas tentativas. Acesso negado.")

# Exemplo de adição de uma opção de recuperação de senha
recuperar_senha = input("Deseja recuperar a senha? (s/n): ")

if recuperar_senha.lower() == "s":
    nova_senha = input("Digite a nova senha: ")
    senha = hashlib.sha256(nova_senha.encode()).hexdigest()
    print("Senha recuperada com sucesso!")
