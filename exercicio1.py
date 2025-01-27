
numero = float(input("Escreva um numero: "))

if numero > 0:
    print("Seu número é positivo")
elif numero == 0:
    print("Seu número é zero")
else:
    print("seu número é negativo")



numero_1 = float(input("Escreva um numero: "))
numero_2 = float(input("Escreva um numero: "))
numero_3 = float(input("Escreva um numero: "))

maior = max(numero_1, numero_2, numero_3)
menor = min(numero_1, numero_2, numero_3)

print(f"O maior número é: {maior}")
print(f"O menor número é: {menor}")