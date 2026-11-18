
contador = 0
usuario = input("Digite seu nome ")
idade = int(input("Digite sua idade "))
entrar = input('Digite \'entrar\' ou \'esperar\'\n')
while True:
    if idade >= 18:
        print("Pode andar no trem")
    elif idade < 18:
        print("Não pode andar no trem")
        break

    comando = input("\n Digite 'andar' ou 'voltar' ou 'parar' ")
    if entrar == "entrar":
        print("Você entrou no trem")

    elif entrar == "esperar":
        print("Espere o proximo trem para entrar")
        break

    if comando == "andar":
        contador = contador + 1
        print(f"🚆 O trem está na estação {contador}.")

        if contador > 5:
            print(f"nome {usuario}, idade {idade}, você parou na estação {contador}, ")
            break

    elif comando == "voltar":
        contador = contador - 1
        print(f"Vc está voltando para uma estação {contador}.")
        if contador == 0:
            break
    elif comando == "parar":
        print(f" O trem parou. {contador}")
        print(f"nome {usuario}, idade {idade}, você parou na estação {contador}, ")
        break
    else:
        print("Comando inválido.")
        