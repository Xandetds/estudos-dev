# Crie uma função em Python chamada 'agrupar_por_paridade' que receba
# uma lista de números inteiros como argumento.
#
# A função deve retornar um dicionário com duas chaves:
# 'pares' -> contendo uma lista de todos os números pares da lista original.
# 'impares' -> contendo uma lista de todos os números ímpares da lista original.

def agrupar_por_paridade(lista):
    pares = []
    impares = []
    dicionario = {'pares': pares, 'impares': impares}
    for numero in lista:
        if numero % 2 == 0:
            pares.append(numero)
        else:
            impares.append(numero)
    return dicionario

lista_usuario = input("Digite uma lista de números inteiros, separadas só por espaços: ")
lista_em_int = list(map(int, lista_usuario.split()))
resultado = agrupar_por_paridade(lista_em_int)
print(resultado)


    
    