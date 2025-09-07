# Crie uma função em Python chamada 'verificar_letra_oculta' que receba
# duas strings: `palavra_secreta` e `letras_adivinhadas`.
#
# A função deve retornar uma NOVA string representando a palavra secreta,
# onde as letras que foram adivinhadas são mostradas e as não adivinhadas
# são substituídas por um traço '_'. Os caracteres não alfabéticos devem ser mantidos.
#
# **Regras:**
# - A comparação de letras deve ser case-insensitive.
# - A string `letras_adivinhadas` contém todas as letras que o jogador já tentou.

def verificar_letra_oculta(palavra_secreta, letras_adivinhadas):
    palavra = ''
    letras_adivinhadas = letras_adivinhadas.lower()
    
    for letra in palavra_secreta:
        if not letra.isalpha():
            palavra += letra
        elif letra.lower() in letras_adivinhadas:
            palavra += letra
        else:
            palavra += '_'
    
    return palavra



palavra_secreta_usuario = input("Digite uma palavra secreta: ")
letras_adivinhadas_usuario = input("Digite uma letra que você acha que está na palavra: ")
resultado = verificar_letra_oculta(palavra_secreta_usuario, letras_adivinhadas_usuario)
print(resultado)