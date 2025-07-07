#
# **Exercício:** Crie uma função em Python que receba a idade de uma pessoa como argumento
# e retorne uma mensagem indicando se ela está apta a votar ou não.
#
# Regras:
# - Idade >= 16: Apta a votar
# - Idade < 16: Não apta a votar

idade_usuario = int(input("Digite a sua idade aqui: "))

def verificar_votacao(idade):
    if idade >= 16:
        return("Você está apto a votar")
    else:    
        return("Você não está apto a votar")


print(verificar_votacao(idade_usuario))



