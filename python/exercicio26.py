# Crie uma função em Python chamada 'analisar_sentenca' que receba
# uma string representando uma única sentença (frase).
#
# A função deve retornar um dicionário com as seguintes informações:
#
# 1. Número de Palavras: Total de palavras na sentença.
# 2. Comprimento Médio das Palavras: A soma dos comprimentos de todas as palavras
#    dividida pelo número total de palavras.
# 3. Contagem de Vogais e Consoantes: Um dicionário aninhado 
#    com a contagem total de vogais e consoantes na sentença (ignorando espaços,
#    números, e pontuações, e sendo case-insensitive).
# 4. Palavras Únicas: Quantas palavras únicas existem na sentença (ignorando case-insensitive).
#
# **Regras:**
# - Considere palavras separadas por espaços.
# - Remova pontuações antes de contar palavras e caracteres.

import string


def analisar_sentenca(frase):
    contagem = {'palavras': 0, 'media_tamanho': 0, 'vogais': 0, 'consoantes': 0, 'palavras_unicas': 0}
    frase_limpa = ''.join(
        caractere.lower() for caractere in frase
        if caractere not in string.punctuation and not caractere.isdigit()
    )

    palavras = frase_limpa.split()
    contagem['palavras'] = len(palavras)

    if palavras:
        soma_comprimentos = sum(len(palavra) for palavra in palavras)
        contagem['media_tamanho'] = soma_comprimentos / len(palavras)

    palavras_unicas = set(palavras)
    contagem['palavras_unicas'] = len(palavras_unicas)

    vogais = 'aeiou'
    consoantes = 'bcdfghjklmnpqrstvwxyz'

    for caractere in frase_limpa:
        if caractere in vogais:
            contagem['vogais'] += 1
        elif caractere in consoantes:
            contagem['consoantes'] += 1

    return contagem

frase_usuario = input("Digite uma frase para análise: ")
resultado = analisar_sentenca(frase_usuario)
print(resultado)
