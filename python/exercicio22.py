# Crie uma função em Python chamada 'lista_para_string' que receba
# uma lista de strings como argumento.
#
# A função deve retornar uma única string que é a concatenação de todos
# os elementos da lista, separados por um espaço.
#
# **Regras:**
# - Se a lista estiver vazia, retorne uma string vazia.

def lista_para_string(lista):
    if lista == []:
        return ''
    lista_em_string = ""
    lista_em_string = " ".join(lista)
    return lista_em_string


lista_usuario = input("Digite uma lista de palavras: ")
resultado = lista_para_string(lista_usuario)
print(resultado)
    
    
    

    
    
