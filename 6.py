# Entrada de dados
n1 = int(input("Digite o primeiro número: "))
n2 = int(input("Digite o segundo número: "))

if n1 > n2:
    print("n1 é MAIOR que n2")
elif n1 < n2:
    print("n1 é MENOR que n2")
else:
    print("n1 é IGUAL a n2")

resultado= n1 * 2
n1 = n1 ** 2

print("\nCálculos com n1:")
print("n1 * 2 =", resultado)
print("n1 ao quadrado =", n1)

resultado= n2 * 2
n2 = n2 ** 2

print("\nCálculos com n2:")
print("n2 * 2 =", resultado)
print("n2 ao quadrado =", n2)
