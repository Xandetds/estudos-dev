numeros = []

for i in range(10):
    numero = int(input("Digite 10 numeros: "))
    numeros.append(numero)


pares = []
impares = []


for num in numeros:
    if num % 2 == 0:
        pares.append(num)
    elif num % 2 != 0:
        impares.append(num)

print(f"Os números pares são: {pares}")
print(f"Os números ímpares são: {impares}")

