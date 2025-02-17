numero = int(input("Digite um numero inteiro para calcular sua fatorial: "))

def fatorial(numero):
    resultado = 1
    for i in range(1, numero + 1):
        resultado *= i
    return resultado

print(f"O fatorial de {numero} é {fatorial(numero)}")
