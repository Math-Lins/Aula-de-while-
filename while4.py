correto = "123456"
senha = input("Digite sua senha: ")
tentativas = 0

while senha!=correto:
    print("Senha incorreta. Digite novamente: ")
    senha = input()
    tentativas = tentativas +1
    if tentativas>=2:
        print("Acesso negado!")
        break
    else:
        print("Acesso liberado!")
