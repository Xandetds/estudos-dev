soma = 0


while True:
    num = float(input("Digite um número (ou um número negativo para sair): "))
    if num < 0:
        break
    soma += num

print(f"A soma de todos os números positivos digitados é: {soma}")



