# Crie uma função em Python chamada 'sortear_varios_elementos' que receba
# uma lista e um número inteiro `quantidade` como argumentos.
#
# A função deve retornar uma NOVA lista contendo `quantidade` elementos
# escolhidos aleatoriamente da lista original. Os elementos podem ser repetidos.
#
# **Regras:**
# - A lista original não estará vazia.
# - A `quantidade` será um número positivo.

import random

def sortear_varios_elementos(lista, quantidade):
    elementos_sorteados = []
    for _ in range(quantidade): 
        elemento_escolhido = random.choice(lista) 
        elementos_sorteados.append(elemento_escolhido) 

    return elementos_sorteados 

lista_usuario_string = input("Digite os elementos da lista (separados por vírgula e espaço, ex: a, b, c): ")
lista_usuario = [item.strip() for item in lista_usuario_string.split(',')]

sorteios_usuario = int(input("Quantos elementos você quer sortear? "))

resultado = sortear_varios_elementos(lista_usuario, sorteios_usuario)

print(resultado)
    
