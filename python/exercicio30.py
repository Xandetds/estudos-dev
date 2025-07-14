# Crie uma função em Python chamada 'sortear_elemento' que receba
# uma lista como argumento.
#
# A função deve retornar um elemento escolhido aleatoriamente da lista.
#
# **Regras:**
# - A lista não estará vazia.

import random

def sortear_elemento(lista):
    return random.choice(lista)

lista = ['elemento 1', 'elemento 2', 'elemento 3']
resultado = sortear_elemento(lista)
print(resultado)