# Crie uma função em Python chamada 'remover_caracteres' que receba
# duas strings: `texto` e `caracteres_para_remover`.
#
# A função deve retornar uma nova string com todos os caracteres
# presentes em `caracteres_para_remover` removidos do `texto` original.


def remover_caracteres(texto, caracteres_para_remover):
    caracteres_removidos = ''
    for caractere in texto:
        if caractere not in caracteres_para_remover:
            caracteres_removidos += caractere
    return caracteres_removidos

texto_usuario = input('Digite um texto: ')
caracteres_para_remover_usuario = input('Digite os caracteres que quer remover do texto: ')
resultado = remover_caracteres(texto_usuario, caracteres_para_remover_usuario)
print(resultado)
                    