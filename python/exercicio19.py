# Crie uma função em Python chamada 'remover_duplicatas' que receba
# uma lista como argumento.
#
# A função deve retornar uma NOVA lista contendo os elementos da lista original,
# mas com todas as duplicatas removidas. A ordem dos elementos restantes pode ser qualquer uma.
#
# **Regras:**
# - Não use `set()` para resolver diretamente. Use loops e condicionais.
#
# **Exemplos de entrada e saída esperada:**
# remover_duplicatas([1, 2, 2, 3, 4, 3, 5]) => [1, 2, 3, 4, 5] (ordem pode variar)
# remover_duplicatas(['a', 'b', 'a', 'c', 'b']) => ['a', 'b', 'c'] (ordem pode variar)
# remover_duplicatas([]) => []