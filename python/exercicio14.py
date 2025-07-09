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