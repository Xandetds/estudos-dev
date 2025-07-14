# Crie uma função em Python chamada 'validar_entrada_ppt' que receba
# uma string `entrada_jogador` como argumento.
#
# A função deve retornar `True` se a `entrada_jogador` for uma das opções válidas
# ('pedra', 'papel', 'tesoura' - case-insensitive), e `False` caso contrário.
#
# **Regras:**
# - A validação deve ignorar maiúsculas/minúsculas.

def validar_entrada_ppt(entrada_jogador):
    entrada_jogador = entrada_jogador.lower()
    if entrada_jogador == 'pedra' or entrada_jogador == 'papel' or entrada_jogador == 'tesoura':
        return True
    else:
        return False

    
entrada_jogador = input("Digite uma entrada para jogar: ").strip()
resultado = validar_entrada_ppt(entrada_jogador)
print(resultado)