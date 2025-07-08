
#Crie uma função em Python chamada `verificar_palindromo` que receba
# uma string como argumento e retorne True se for um palíndromo, e False caso contrário.
#
# Um palíndromo é uma palavra ou frase que é lida da mesma forma de trás para frente,
# ignorando espaços e diferenças entre maiúsculas e minúsculas.
#
# **Regras:**
# - Desconsidere letras maiúsculas/minúsculas.
# - Desconsidere espaços em branco.
#
# **Exemplos de entrada e saída esperada:**
# verificar_palindromo("arara")          => True
# verificar_palindromo("Ame o poema")    => True
# verificar_palindromo("Python")         => False
#
# **Dica:** Use os métodos `.lower()` e `.replace()` da string para facilitar o tratamento.

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
        
    