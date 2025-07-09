# Crie uma função chamada `maior_valor` que receba uma lista de números inteiros
# e retorne o maior número presente na lista.
#
# **Regras:**
# - A lista sempre terá pelo menos um número.
# - Não use a função `max()` do Python (faça usando lógica e comparação).


def maior_valor(numeros):
    lista_numeros = numeros[0]
    for numero in numeros:
        if numero > lista_numeros:
            lista_numeros = numero
    return lista_numeros
    
lista = [10, 5, 8, 20, 3]
resultado = maior_valor(lista)
print(f"o seu maior valor é: {resultado}")


def menor_valor(numeros):
    lista_numeros = numeros[0]
    for numero in numeros:
        if numero < lista_numeros:
            lista_numeros = numero
    return lista_numeros


lista = [10, 5, 8, 20, 3]
resultado = menor_valor(lista)
print(f"o seu menor valor é: {resultado}")