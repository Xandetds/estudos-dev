# Crie uma função chamada analisar_numeros que receba uma lista de números inteiros
# e retorne um dicionário com as seguintes informações:
#
# "pares" → quantidade de números pares na lista
# "ímpares" → quantidade de números ímpares
# "média" → valor médio (soma ÷ quantidade)


def analisar_numeros(numeros):
    contagem = {'pares': 0, 'impares': 0}
    
    for numero in numeros:
        if numero % 2 == 0:
            contagem ['pares'] += 1
        else:
            contagem ['impares'] += 1
    return contagem



entrada = input("Digite vários números separados por espaço: ")
numeros = [int(n) for n in entrada.split()]

media = sum(numeros) / len(numeros)

resultado = analisar_numeros(numeros) 
resultado['média'] = media
print(resultado)