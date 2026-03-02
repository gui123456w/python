usuario = ' '
senha = ''
tentativas = 0

while (usuario != "neymar" and senha !=  '12345') and tentativas < 3:
    usuario = input("Informe sua senha: ")
    senha = input("digite sua senha : ")
    tentativas += 1

if usuario != "neymar" and senha != "12345 ":
    print("tente novamente")
else:
    print("login perfeito")
