# Crie uma função em Python chamada 'combinar_palavras' que receba
# duas ou mais strings como argumentos (pode ser uma quantidade variável de argumentos).
#
# A função deve retornar uma única string que é a concatenação de todas as strings,
# separadas por um espaço.

def combinar_palavras(*args):
    return " ".join(args)

string1 = input("Digite uma palavra: ")
string2 = input("Digite outra palavra: ")
string3 = input("Digite outra palavra: ")
string4 = input("Digite outra palavra: ")
string5 = input("Digite outra palavra: ")

resultado = combinar_palavras(string1, string2, string3, string4, string5)
print(resultado)