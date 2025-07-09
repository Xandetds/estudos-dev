# Crie uma função chamada `tipos_de_caracteres` que receba uma string
# e retorne **quantos tipos diferentes de caracteres ela contém**, entre:
# - Letras maiúsculas
# - Letras minúsculas
# - Números
# - Especiais (!@#$%&*?, etc.)

def tipos_de_caracteres(texto):
    contagem = {'especiais': 0, 'numeros': 0, 'maiusculas': 0, 'minusculas': 0}
    especiais = '!@#$%&.,;:(){}[]*?'

    for caractere in texto:
        if caractere in especiais:
            contagem['especiais'] += 1
        elif caractere.isdigit():
            contagem['numeros'] += 1
        elif caractere.isupper():
            contagem['maiusculas'] += 1
        elif caractere.islower():
            contagem['minusculas'] += 1

    return contagem


texto_usuario = input("Digite um texto: ")
resultado = tipos_de_caracteres(texto_usuario)
print(resultado)
 