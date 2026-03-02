senha_correta = "python123"
tentativas = 3

print("=== Sistema de Login ===")

while tentativas > 0:
    senha = input("Digite a senha: ")

    if senha == senha_correta:
        print("Acesso permitido! Bem-vindo!")
        break
    else:
        tentativas -= 1
        print("Senha incorreta!")

        if tentativas > 0:
            print(f"Tentativas restantes: {tentativas}")
        else:
            print("Você errou 3 vezes. Acesso BLOQUEADO!")

