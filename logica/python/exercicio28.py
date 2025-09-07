# Crie uma função em Python chamada 'contar_caractere_case_insensitive' que receba
# uma string `texto` e um caractere `letra` como argumentos.
#
# A função deve retornar o número de vezes que a `letra` aparece no `texto`,
# ignorando se é maiúscula ou minúscula.


def contar_caractere_case_insensitive(texto, letra):
    letra = letra.lower()
    contagem = 0
    for caractere in texto:
        if caractere.lower() == letra:
            contagem += 1
    return contagem

texto_usuario = input("Digite um texto: ")
letra_usuario = input("Digite uma letra: ")
resultado = contar_caractere_case_insensitive(texto_usuario, letra_usuario)
print(resultado)
        