def ler_idade():
    while True:
        try:
            idade = int(input("Digite a idade: "))
            if idade > 0:
                return idade
        except ValueError:
            pass
        print("Idade inválida, tente novamente.")


def ler_cnh():
    while True:
        resposta = input("Possui CNH? (s/n): ").strip().lower()
        if resposta in ("s", "n"):
            return resposta == "s"
        print("Responda apenas com 's' ou 'n'.")


def avaliar(idade, tem_cnh):
    motivos = []
    if idade < 18:
        motivos.append("não ter idade mínima")
    if not tem_cnh:
        motivos.append("dirigir sem habilitação")

    if not motivos:
        return "Pode seguir, boa viagem!"
    return "Não pode dirigir, carro apreendido por " + " e ".join(motivos) + "."


print("======= Blitz da Polícia =======")
idade = ler_idade()
tem_cnh = ler_cnh()
print(avaliar(idade, tem_cnh))