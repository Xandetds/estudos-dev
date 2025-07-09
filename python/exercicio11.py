# Crie uma função em Python chamada `tem_numero` que receba uma string
# como argumento e retorne True se essa string contiver **pelo menos um número** (de 0 a 9),
# e False caso contrário.
#
# **Regras:**
# - A função deve verificar se **algum caractere** da string é um número.
# - Não use expressões regulares (regex).


def tem_numero(texto):
    for caractere in texto:
        if caractere.isdigit():
            return True
    return False
        
digite = input("Digite um texto: ")
resultado = tem_numero(digite)
print(resultado)