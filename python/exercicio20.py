# Crie uma função em Python chamada 'listas_sao_iguais' que receba
# duas listas como argumentos.
#
# A função deve retornar `True` se as duas listas contiverem **exatamente os mesmos elementos**,
# independentemente da ordem. Retorne `False` caso contrário.
#
# **Regras:**
# - As listas podem ter tamanhos diferentes se houver duplicatas.
# - Não use a conversão direta para `set()` para comparar. Pense em contar ocorrências ou ordenar.
#
# **Exemplos de entrada e saída esperada:**
# listas_sao_iguais([1, 2, 3], [3, 2, 1]) => True
# listas_sao_iguais([1, 2, 2], [2, 1, 2]) => True
# listas_sao_iguais([1, 2], [1, 2, 3]) => False
# listas_sao_iguais(['a', 'b'], ['b', 'c']) => False