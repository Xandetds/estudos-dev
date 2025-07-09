# Crie uma função em Python chamada 'filtrar_pares' que receba
# uma lista de números inteiros como argumento.
#
# A função deve retornar uma NOVA lista contendo APENAS os números pares da lista original.


def filtrar_pares(numeros):
    pares = []
    for numero in numeros:
        if numero % 2 == 0:
            pares.append(numero)
    return pares

entrada = input("Digite vários números separados por espaço: ")
numeros_do_usuario = [int(n) for n in entrada.split()]
numeros_pares_encontrados = filtrar_pares(numeros_do_usuario)
print("Números pares encontrados:", numeros_pares_encontrados)




            
