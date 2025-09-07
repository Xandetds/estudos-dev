# Crie uma função em Python chamada contar_letras que recebe uma frase (string)
# como parâmetro e retorna um dicionário com a quantidade de vezes que cada letra
# aparece na frase.
#
#  Regras:
# - Ignorar maiúsculas/minúsculas (deixar tudo minúsculo).
# - Ignorar espaços, números e pontuação.
# - Contar somente as letras do alfabeto (de A a Z).

import string

frase = input("Digite uma frase: ")

def contar_letras(frase):
    frase = frase.lower()
    letras = {}
    
    for caractere in frase:
        if caractere in string.ascii_lowercase: 
            if caractere in letras:
                letras[caractere] += 1
            else:
                letras[caractere] = 1
    return letras

print(contar_letras(frase))
            

