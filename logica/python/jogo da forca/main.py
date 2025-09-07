# Jogo da Forca em Python (Terminal)
#
# **Objetivo:** Implementar uma versão do jogo da forca no terminal. O programa escolhe
# uma palavra secreta, e o jogador tenta adivinhá-la letra por letra com chances limitadas.
#
# **Funcionalidades:**
# 1. Banco de palavras e sorteio aleatório da palavra secreta.
# 2. Exibição da palavra oculta (com traços para letras não adivinhadas).
# 3. Gerenciamento de chances (letras erradas diminuem chances).
# 4. Verificação de letras digitadas (acerto, erro, letra já usada).
# 5. Condições de vitória e derrota.
# 6. Feedback ao jogador (letras usadas, chances restantes).

from funcoes_jogo import (
    escolher_palavra,
    mostrar_palavra_oculta,
    letra_ja_usada,
    verificar_vitoria,
    mensagem_final
)

lista_palavras = ["banana", "morango", "melancia", "abacaxi", "uva", "laranja"]
palavra_secreta = escolher_palavra(lista_palavras)

letras_usadas = []
chances = 6
vitoria = False

while chances > 0 and not vitoria:
    print("\nPalavra:", mostrar_palavra_oculta(palavra_secreta, letras_usadas))
    print("Letras usadas:", " ".join(letras_usadas))
    print("Chances restantes:", chances)
    
    tentativa = input("Digite uma letra: ").strip()

    if len(tentativa) != 1 or not tentativa.isalpha():
        print("Digite apenas uma letra válida.")
        continue

    tentativa = tentativa.lower()

    if letra_ja_usada(tentativa, letras_usadas):
        print("Você já tentou essa letra.")
        continue

    letras_usadas.append(tentativa)

    if tentativa not in palavra_secreta.lower():
        print("Letra incorreta.")
        chances -= 1

    vitoria = verificar_vitoria(palavra_secreta, letras_usadas)

mensagem_final(vitoria, palavra_secreta)
