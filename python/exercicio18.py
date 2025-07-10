# Crie uma função em Python chamada 'contar_ocorrencias' que receba
# uma lista e um elemento como argumentos.
#
# A função deve retornar o número de vezes que o elemento aparece na lista.
#
# **Regras:**
# - Não use o método `.count()` da lista. Faça a contagem usando um loop.

def contar_ocorrencias(lista, elemento):
    contador = 0
    for item in lista:
        if item == elemento:
            contador += 1
    return contador

lista_usuario = [1, 2, 3, 2, 4, 2]
resultado = contar_ocorrencias(lista_usuario, 2)
print(resultado) 