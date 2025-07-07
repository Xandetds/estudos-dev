numeros= []

for i in range(8):
    numero = int(input("Digite 8 números: "))
    numeros.append(numero)

soma = sum(numeros)
print(f"A soma dos números digitados é: {soma}")

maior = max(numeros)
menor = min(numeros)

print(f"O maior número digitado é: {maior}")
print(f"O menor número digitado é: {menor}")

