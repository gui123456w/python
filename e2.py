idade = (int(input("Digite a idade: ")))
temcarteira = input ("se tiver carteira de motorista s/n")

if idade >= 18 and temcarteira == "s":
    print("pode dirigir")
else:
    print("não dirigir")

