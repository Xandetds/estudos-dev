# Crie uma função em Python chamada `validar_senha` que receba
# uma string (representando uma senha) como argumento.
#
# A função deve verificar se a senha atende a UM dos seguintes conjuntos de regras
# (ou seja, a senha deve ser forte OU média OU fraca, mas não pode ser inválida).
# Retorne uma string indicando a força da senha: "Forte", "Média", "Fraca" ou "Inválida".
#
# **Regras de Força da Senha:**
# 1. Senha **FORTE**:
#    - Mínimo de 8 caracteres.
#    - Conter pelo menos uma letra maiúscula.
#    - Conter pelo menos uma letra minúscula.
#    - Conter pelo menos um número.
#    - Conter pelo menos um caractere especial (ex: !, @, #, $, %, &, *...).
#
# 2. Senha **MÉDIA**:
#    - Mínimo de 6 caracteres.
#    - Conter pelo menos 3 dos 4 tipos de caracteres (maiúscula, minúscula, número, especial).
#
# 3. Senha **FRACA**:
#    - Mínimo de 4 caracteres.
#    - Conter apenas 1 ou 2 tipos de caracteres (entre os 4 acima).
#
# 4. Senha **INVÁLIDA**:
#    - Menos de 4 caracteres.

def validar_senha(senha):
    forte = 'Sua senha é forte'
    media = 'Sua senha é média'
    fraca = 'Sua senha é fraca'
    invalida = 'Sua senha é inválida'

    tem_maiuscula = False
    tem_minuscula = False
    tem_numero = False
    tem_especial = False

    especiais = '!@#$%&.,;:(){}[]*?'

    for caractere in senha:
        if caractere.isupper():
            tem_maiuscula = True
        if caractere.islower():
            tem_minuscula = True
        if caractere.isdigit():
            tem_numero = True
        if caractere in especiais:
            tem_especial = True

    tipos = sum([tem_maiuscula, tem_minuscula, tem_numero, tem_especial])

    if len(senha) < 4:
        return invalida
    elif len(senha) >= 8 and tipos == 4:
        return forte
    elif len(senha) >= 6 and tipos >= 3:
        return media
    elif len(senha) >= 4 and tipos in [1, 2]:
        return fraca
    else:
        return invalida
    


senha_usuario = input("Digite uma senha: ")
resultado = validar_senha(senha_usuario)
print(resultado)

