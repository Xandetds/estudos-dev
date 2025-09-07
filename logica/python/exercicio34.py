# Crie uma função em Python chamada 'escolher_opcao_aleatoria' que receba
# uma lista de strings (opções) como argumento.
#
# A função deve retornar uma opção escolhida aleatoriamente da lista.
#
# **Regras:**
# - A lista de opções não estará vazia.
# - A escolha deve ser puramente aleatória.

import random

def escolher_opcao_aleatoria(opcoes):
    return random.choice(opcoes)
    
opcoes_str = input("Digite opções separadas por um espaço: ")
opcoes_user = opcoes_str.split()
resultado = escolher_opcao_aleatoria(opcoes_user)
print(resultado)
