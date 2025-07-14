import random

def escolher_palavra(lista_palavras):
    return random.choice(lista_palavras)

def mostrar_palavra_oculta(palavra_secreta, letras_usadas):
    palavra = ''
    for letra in palavra_secreta:
        if not letra.isalpha():
            palavra += letra
        else:
            letra_foi_adivinhada = False
            for l in letras_usadas:
                if letra.lower() == l.lower():
                    letra_foi_adivinhada = True
                    break
            if letra_foi_adivinhada:
                palavra += letra
            else:
                palavra += '_'
    return palavra

def letra_ja_usada(letra, letras_usadas):
    for l in letras_usadas:
        if letra.lower() == l.lower():
            return True
    return False

def verificar_vitoria(palavra_secreta, letras_usadas):
    for letra in palavra_secreta:
        if letra.isalpha():
            foi_adivinhada = False
            for l in letras_usadas:
                if letra.lower() == l.lower():
                    foi_adivinhada = True
                    break
            if not foi_adivinhada:
                return False
    return True

def mensagem_final(vitoria, palavra_secreta):
    if vitoria:
        print("🎉 Parabéns! Você venceu!")
    else:
        print("💀 Suas chances acabaram.")
    
    print("A palavra era:", palavra_secreta)
