# Crie uma função em Python chamada 'determinar_vencedor_par_impar' que receba
# duas strings: `escolha_jogador1` e `escolha_jogador2`,
# e dois números inteiros: `numero_jogador1` e `numero_jogador2`.
#
# As escolhas (`escolha_jogadorX`) podem ser 'par' ou 'ímpar'.
#
# A função deve determinar a soma dos dois números (`numero_jogador1` + `numero_jogador2`)
# e verificar se o resultado é par ou ímpar.
# Com base nisso e nas escolhas dos jogadores, retorne uma string indicando o resultado:
# 'Empate', 'Jogador 1 Venceu', ou 'Jogador 2 Venceu'.
#
# **Regras:**
# - Se a soma for par: vence quem escolheu 'par'.
# - Se a soma for ímpar: vence quem escolheu 'ímpar'.
# - Em caso de empate nas escolhas ('par' e 'par', ou 'ímpar' e 'ímpar' para a soma),
#   o resultado é determinado pela paridade da soma.
# - Suponha que as entradas de escolha serão sempre 'par' ou 'ímpar' (em minúsculas)
#   e os números serão inteiros.