# Crie uma função em Python chamada `verificar_palindromo` que receba
# uma string como argumento e retorne True se for um palíndromo, e False caso contrário.
#
# Um palíndromo é uma palavra ou frase que é lida da mesma forma de trás para frente,
# ignorando espaços e diferenças entre maiúsculas e minúsculas.
#
# **Regras:**
# - Desconsidere letras maiúsculas/minúsculas.
# - Desconsidere espaços em branco.


def verificar_palindromo(palavra):
    palavra = palavra.lower()
    palavra = palavra.replace(' ','')
    if palavra == palavra[::-1]:
        return True
    else:
        return False
    
entrada = input("Digite uma palavra: ")
palavra = verificar_palindromo(entrada)
print(palavra)
        
    