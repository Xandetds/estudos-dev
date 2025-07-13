# Crie uma função em Python chamada 'remover_letra_de_palavras' que receba
# uma lista de palavras `lista_palavras` e um caractere `letra_para_remover`.
#
# A função deve retornar uma NOVA lista de palavras, onde cada palavra da lista original
# teve todas as ocorrências da `letra_para_remover` removidas (case-insensitive).

def remover_letra_de_palavras(lista_palavras, letra_para_remover):
    letra_para_remover = letra_para_remover.lower()
    lista_palavras_removidas = []

    for palavra in lista_palavras:
        nova_palavra = ''
        for caractere in palavra:
            if caractere.lower() != letra_para_remover:
                nova_palavra += caractere
        lista_palavras_removidas.append(nova_palavra)

    return lista_palavras_removidas


lista_palavras_usuario = input("Digite uma lista de palavras separadas por espaço: ")
letra_para_remover_usuario = input("Digite a letra que deseja remover: ")
lista = lista_palavras_usuario.split()
resultado = remover_letra_de_palavras(lista, letra_para_remover_usuario)
print(resultado)