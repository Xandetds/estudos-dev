#
# Jogo de Pedra, Papel e Tesoura (Terminal)
#
# **Objetivo:** Implementar uma versão do clássico jogo "Pedra, Papel e Tesoura"
# que roda no terminal. O jogador joga contra o computador.
#
# **Funcionalidades:**
# 1. Escolha do Jogador: O programa deve pedir ao jogador para digitar sua escolha
#    ('pedra', 'papel' ou 'tesoura').
# 2. Escolha do Computador: O computador deve fazer sua escolha aleatoriamente.
# 3. Validação de Entrada: A entrada do jogador deve ser validada para garantir
#    que é uma opção válida.
# 4. Determinação do Vencedor: A lógica do jogo deve determinar se o jogador venceu,
#    o computador venceu, ou se houve um empate.
# 5. Múltiplas Rodadas: O jogo deve permitir que o jogador jogue várias rodadas,
#    mantendo uma pontuação (placar) de vitórias, derrotas e empates.
# 6. Opção de Sair: O jogador deve poder sair do jogo a qualquer momento.
# 7. Feedback ao Jogador: Exibir as escolhas de ambos, o resultado da rodada e o placar atual.

from funcoes_jogo import (escolher_opcao_aleatoria, validar_entrada_ppt, determinar_vencedor_ppt)


vitorias_jogador = 0
derrotas_jogador = 0
empates = 0

opcoes_validas_jogo = ['pedra', 'papel', 'tesoura'] 

print("Bem-vindo ao Jogo de Pedra, Papel e Tesoura!")
print("Digite 'sair' a qualquer momento para encerrar o jogo.")

while True:
    print(f"\n--- Placar: Vitórias: {vitorias_jogador} | Derrotas: {derrotas_jogador} | Empates: {empates} ---")

    escolha_jogador1 = input('Digite sua escolha ("pedra", "papel" ou "tesoura"): ').lower() 

    if escolha_jogador1 == 'sair':
        print("Obrigado por jogar! Placar final:")
        print(f"Vitórias: {vitorias_jogador} | Derrotas: {derrotas_jogador} | Empates: {empates}")
        break 

    if validar_entrada_ppt(escolha_jogador1):
        escolha_jogador2 = escolher_opcao_aleatoria(opcoes_validas_jogo)

        print(f"Você escolheu: {escolha_jogador1}")
        print(f"O computador escolheu: {escolha_jogador2}")

        resultado = determinar_vencedor_ppt(escolha_jogador1, escolha_jogador2)
        print(f"Resultado da rodada: {resultado}")

        if resultado == 'Jogador 1 Venceu':
            vitorias_jogador += 1
        elif resultado == 'Jogador 2 Venceu':
            derrotas_jogador += 1
        else: 
            empates += 1
    else:
        print("Escolha inválida. Por favor, digite 'pedra', 'papel' ou 'tesoura'.")