print("=======Blitz da Policia seja bem vindo=========  ")
print("=======Digite sua idade e se possui CNH=========")

idade = int(input("Digite a idade: "))
cnh = input("Possui cartão de condução? (s/n): ")

while idade and cnh == " ":
    idade = int(input("Digite a idade: "))
    cnh = input("Possui cartão de condução? (s/n): ")
if idade >= 18 and cnh == "s":
    print("Pode seguir boa viagem!")
elif idade > 18 and cnh == "n":
    print("Não pode dirigir, tera carro apreendido!")
elif idade < 18 and cnh == "s":
    print("Não pode dirigir, tera carro apreendido por não ter idade minima!")
elif idade < 18 and cnh == "n":
    print("Não pode dirigir, tera carro apreendido por não ter idade minima e dirigir sem habilitação!")
else: 
    print("Faça outro chamado, digite novamente! ")
