import random

def escolher_opcao_aleatoria(opcoes):
    return random.choice(opcoes)
    

def validar_entrada_ppt(entrada_jogador):
    entrada_jogador = entrada_jogador.lower()
    if entrada_jogador == 'pedra' or entrada_jogador == 'papel' or entrada_jogador == 'tesoura':
        return True
    else:
        return False

def determinar_vencedor_ppt(escolha_jogador1, escolha_jogador2):
    if escolha_jogador1 == escolha_jogador2:
        return 'Empate'
    elif (escolha_jogador1 == 'pedra' and escolha_jogador2 == 'tesoura'):
        return 'Jogador 1 Venceu'
    elif (escolha_jogador1 == 'papel' and escolha_jogador2 == 'pedra'):
        return 'Jogador 1 Venceu'
    elif (escolha_jogador1 == 'tesoura' and escolha_jogador2 == 'papel'):
        return 'Jogador 1 Venceu'
    else:
        return 'Jogador 2 Venceu'
    
