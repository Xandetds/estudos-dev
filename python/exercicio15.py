# Crie uma função em Python chamada 'analisar_texto' que receba
# uma string (um texto, frase ou parágrafo) como argumento.
#
# A função deve retornar um dicionário com as seguintes informações sobre o texto:
#
# 1. **Número Total de Caracteres:** (incluindo espaços, pontuações, etc.)
# 2. **Número Total de Palavras:** (separadas por espaços)
# 3. **Número Total de Frases:** (considerando que uma frase termina com '.', '!', ou '?')
# 4. **Frequência de Vogais:** (um dicionário dentro do dicionário principal, contando 'a', 'e', 'i', 'o', 'u' - case-insensitive)
#
# **Regras:**
# - Para contar frases, considere que elas terminam com '.', '!', ou '?'.
# - A contagem de vogais deve ser case-insensitive.


def analisar_texto(texto):
    vogais = {'vogal a': 0,  'vogal e': 0, 'vogal i': 0, 'vogal o': 0, 'vogal u': 0}
    contagem = {'caracteres': 0, 'palavras': 0, 'frases': 0}
    for caractere in texto:
        if caractere.lower() == 'a':
            vogais['vogal a'] += 1
        elif caractere.lower() == 'e':
            vogais['vogal e'] += 1
        elif caractere.lower() == 'i':
            vogais['vogal i'] += 1
        elif caractere.lower() == 'o':
            vogais['vogal o'] += 1
        elif caractere.lower() == 'u':
            vogais['vogal u'] += 1
    
    contagem['caracteres'] = len(texto)
    contagem['palavras'] = len(texto.split())
    contagem['frases'] = texto.count('.') + texto.count('!') + texto.count('?')    
    
    return {'contagem': contagem, 'frequencia de vogais': vogais}

    
texto_usuario = input("Digite um texto: ")
resultado = analisar_texto(texto_usuario)
print(resultado)
    
    