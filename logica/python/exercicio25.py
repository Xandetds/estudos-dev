# Crie uma função em Python chamada 'contar_vogais_consoantes_palavra' que receba
# uma única palavra (string) como argumento.
#
# A função deve retornar um dicionário com a contagem de vogais e consoantes na palavra.
#
# **Regras:**
# - Considere as vogais: 'a', 'e', 'i', 'o', 'u' (case-insensitive).
# - Tudo que não for vogal (e for letra) é consoante.
# - Ignore números, espaços e caracteres especiais.

def contar_vogais_consoantes_palavra(texto):
    contagem = {'vogais': 0, 'consoantes': 0}
    vogais = 'aeiou'
    consoantes = 'bcdfghjklmnpqrstvwxyz'
    for letra in texto:
        letra = letra.lower()   
        if letra in vogais:
            contagem['vogais'] += 1
        elif letra in consoantes:
            contagem['consoantes'] += 1
    return contagem


texto_usuario = input("Digite um texto: ")
resultado = contar_vogais_consoantes_palavra(texto_usuario)
print(resultado)