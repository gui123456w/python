n1 = int(input("digite um numero "))
n2 = int(input("digite um numero "))

if n1 > n2:
    print(f"n1 maior que n2")
elif n1 < n2:
    print(f"n1 menor que n2")
else:
    print(f"n1 igual a n2")

resultado = n1 * 2
n1 = n1 ** 2

print(f"\n calculos a seguir",f"\nN1* 2 = ",resultado,f"\nn1 ** 2 = ",n1)

resultado = n2 * 2
n2 = n2 ** 2

print(f"\ncalculos",f"n2* 2 = ",resultado,f"\nn2 ** 2 = ",n2)
print(f"\nResultado da n1: ",n1, f"\nResultado da n2 :",n2, f"\nObrigado por utilizar! ")

