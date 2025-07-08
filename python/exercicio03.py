# **Exercício:** Crie uma função em Python que receba uma string (frase/parágrafo)
# e retorne um dicionário com a contagem de cada palavra.
#
# Regras:
# - A contagem deve ser case-insensitive (ignorar maiúsculas/minúsculas).
# - Pontuações (vírgulas, pontos, etc.) devem ser ignoradas.
#
# Exemplo:
# Entrada: "Olá mundo, este é um exemplo. Olá!"
# Saída: {'olá': 2, 'mundo': 1, 'este': 1, 'é': 1, 'um': 1, 'exemplo': 1}

import string

def contar_palavras(texto):
    texto = texto.lower()
    for pontuacao in string.punctuation:
        texto = texto.replace(pontuacao, '')
    palavras = texto.split()
    contagem = {}
    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1
    return contagem

print(contar_palavras("Olá, mundo, tudo bem? olá!!!!"))