# Crie uma função em Python chamada 'encontrar_segundo_maior' que receba
# uma lista de números inteiros como argumento.
#
# A função deve retornar o segundo maior número presente na lista.
#
# **Regras:**
# - A lista terá sempre pelo menos dois números.
# - Não use a função `sort()` ou `sorted()` do Python. Faça usando lógica de comparação.
# - Os números na lista podem ser repetidos.

def encontrar_segundo_maior(lista):
    maior = float('-inf')
    segundo_maior = float('-inf')

    for numero in lista:
        if numero > maior:
            segundo_maior = maior
            maior = numero
        elif numero > segundo_maior and numero != maior:
            segundo_maior = numero

    return segundo_maior

entrada = input("Digite uma lista de números separados por espaço: ")
lista_usuario = list(map(int, entrada.split()))
resultado = encontrar_segundo_maior(lista_usuario)
print(resultado)