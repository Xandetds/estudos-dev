# Crie uma função em Python chamada 'inverter_lista' que receba uma lista como argumento.
#
# A função deve retornar uma NOVA lista com os elementos da lista original em ordem inversa.
#
# **Regras:**
# - Não use o método `.reverse()` ou `[::-1]` da lista. Faça a inversão usando um loop.


def inverter_lista(lista):
    invertida = []
    for i in range(len(lista) - 1, -1, -1):
        invertida.append(lista[i])
    return invertida

print(inverter_lista([1, 2, 3, 4, 5]))      
print(inverter_lista([52, 53, 54, 55, 56]))  
