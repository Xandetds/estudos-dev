# Crie uma função chamada `tem_caractere_especial` que receba uma string
# e retorne True se ela contiver **pelo menos um caractere especial**, e False se não tiver nenhum.
#
# **Consideramos como caracteres especiais:** !, @, #, $, %, &, *, ?, etc.
# (Você pode definir uma string com esses símbolos para comparar).
#
# **Exemplos de entrada e saída esperada:**
# tem_caractere_especial("senha123!")     => True
# tem_caractere_especial("teste@2024")    => True
# tem_caractere_especial("apenasletras")  => False


def um_caractere_especial(frase):
    especiais = "!@#$%&*?"
    for caractere in frase:
        if caractere in especiais:
            return True
    return False

frase_usuario = input("Digite uma frase: ")
resultado = um_caractere_especial(frase_usuario)
print(resultado)