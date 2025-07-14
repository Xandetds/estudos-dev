# funcoes_gerador.py
# Contém as funções auxiliares para o Gerador de Histórias Aleatórias.

import random 

def sortear_elemento(lista):
    return random.choice(lista)

def combinar_elementos_em_historia(personagem, verbo, objeto, local):
    historia_final = f"{personagem} {verbo} {objeto} em {local}."
    return historia_final
    

