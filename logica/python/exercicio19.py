# Crie uma função em Python chamada 'remover_duplicatas' que receba
# uma lista como argumento.
#
# A função deve retornar uma NOVA lista contendo os elementos da lista original,
# mas com todas as duplicatas removidas. A ordem dos elementos restantes pode ser qualquer uma.
#
# **Regras:**
# - Não use `set()` para resolver diretamente. Use loops e condicionais.

def remover_duplicatas(lista):
    sem_duplicatas = []
    for item in lista:
        if item not in sem_duplicatas:
            sem_duplicatas.append(item)
    return sem_duplicatas
    
        
lista = [1, 2, 2, 3, 4, 3, 5, 1]
resultado = remover_duplicatas(lista)
print(resultado) 