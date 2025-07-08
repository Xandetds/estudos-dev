# Crie uma função chamada contar_vogais_consoantes que receba uma frase como entrada
# e retorne um dicionário com duas chaves:
# "vogais" → contendo a quantidade total de vogais.
# "consoantes" → contendo a quantidade total de consoantes.
#
# Regras:
# - Ignorar maiúsculas/minúsculas.
# - Ignorar acentos, espaços, números e pontuações.
# - Contar somente letras do alfabeto de A a Z.
# - As vogais são: a, e, i, o, u.
# - Todo o resto (que for letra) é consoante.

import string

def contar_vogais_consoantes(frase):
    frase = frase.lower()
    vogais = {'a', 'e', 'i', 'o', 'u'}  
    contagem = {'vogais': 0, 'consoantes': 0}    
    
    for caractere in frase:
        if caractere in string.ascii_lowercase:     
            if caractere in vogais:
                contagem ['vogais'] += 1
            else:
                contagem ['consoantes'] += 1
    return contagem

frase = input("Digite uma frase: ")
resultado = contar_vogais_consoantes(frase)
print(resultado)
