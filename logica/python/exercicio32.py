# Crie uma função em Python chamada 'gerar_frase_personalizada' que receba
# três strings como argumentos: `nome`, `verbo` e `objeto`.
#
# A função deve retornar uma frase no formato:
# "[Nome] [verbo] [objeto]."

def gerar_frase_personalizada(nome, verbo, objeto):
    return " ".join((nome, verbo, objeto))


nome_usuario = input("Digite o nome (ex: O cachorro): ")
verbo_usuario = input("Digite o verbo (ex: corre atrás): ")
objeto_usuario = input("Digite o objeto (ex: da bola): ")
resultado = gerar_frase_personalizada(nome_usuario, verbo_usuario, objeto_usuario)
print(resultado)
