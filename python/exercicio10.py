# Crie uma função chamada `contar_maiusculas_minusculas` que receba
# uma string como argumento e retorne duas informações:
# - A quantidade de letras maiúsculas na string.
# - A quantidade de letras minúsculas na string.


def contar_maiusculas_minusculas(frase):
    maiusculas = 0
    minusculas = 0
    for letra in frase:
        if letra.isupper():
            maiusculas += 1
        elif letra.islower():
            minusculas += 1
    return (maiusculas, minusculas)    
    
digite = input("Digite uma frase: ")
resultado = contar_maiusculas_minusculas(digite)
print(resultado)


