a = int(input("Digite a primeira linha: "))
b = int(input("Digite a segunda linha: "))
c = int(input("Digite a terceira linha: "))
maior = a

if b > maior:
    maior = b

if c > maior:
    maior = c

print("Numero maior é", maior)

