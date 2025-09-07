# Gerador de Histórias Aleatórias em Python (Terminal)
#
# **Objetivo:** Criar um programa que gera histórias curtas e aleatórias
# combinando elementos pré-definidos (personagens, ações, objetos, locais).
#
# **Funcionalidades:**
# 1. Armazenar listas de personagens, ações, objetos e locais.
# 2. Sortear um elemento de cada categoria aleatoriamente.
# 3. Combinar os elementos sorteados para formar uma frase/história coerente.
# 4. Permitir ao usuário gerar novas histórias ou sair.

from funcoes_gerador import (sortear_elemento, combinar_elementos_em_historia)

personagens_str = input('Digite nomes de personagens separados por um espaço: ')
verbos_str = input('Digite verbos separados por um espaço: ')
objetos_str = input('Digite nomes de objetos separados por um espaço: ')
locais_str = input('Digite nomes de locais separados por um espaço: ')

personagens = personagens_str.split()
verbos = verbos_str.split()
objetos = objetos_str.split()
locais = locais_str.split()

personagem_sorteado = sortear_elemento(personagens)
verbo_sorteado = sortear_elemento(verbos)
objeto_sorteado = sortear_elemento(objetos)
local_sorteado = sortear_elemento(locais)

resultado = combinar_elementos_em_historia(personagem_sorteado, verbo_sorteado, objeto_sorteado, local_sorteado)
print(resultado)

