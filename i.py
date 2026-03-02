numero = int(input(f"Digite um numnero "))

resultado = numero + 1
print(numero + 1)

n2 = int(input(f"Digite outro numeror"))
resultado1 = numero + 1
print(numero + 1)

if numero >= n2 :
    resultado = n2 + 1
    print(numero + 1)
    resultado1 = numero * 2
    print("numero digitado: ",numero * 2, )

elif numero == n2:
    resultado = numero* n2
    print(f"numero ** n2 ",resultado)
else:
    print(f"numero invalido por causa que numero é menor que n2 : ",resultado)
print(f"\nFinal do codigo o Numero digitado é  de ",resultado)