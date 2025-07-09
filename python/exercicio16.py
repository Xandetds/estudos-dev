# Crie uma função em Python chamada 'eh_ano_bissexto' que receba
# um número inteiro (representando um ano) como argumento.
#
# A função deve retornar `True` se o ano for bissexto, e `False` caso contrário.
#
# **Regras:**
# - Um ano é bissexto se for divisível por 4.
# - EXCEÇÃO: Anos divisíveis por 100 NÃO são bissextos, a menos que sejam divisíveis por 400.


def eh_ano_bissexto(ano):
    if ano % 400 == 0:
        return True
    elif ano % 100 == 0:
        return False
    elif ano % 4 == 0:
        return True
    else:
        return False

ano_usuario = int(input("Digite um ano: "))
resultado = eh_ano_bissexto(ano_usuario)
print(resultado)