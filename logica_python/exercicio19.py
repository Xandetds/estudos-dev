def contar_vogais(texto):
    vogais = "aeiouAEIOU"
    contador = 0

    for letra in texto:
        if letra in vogais:
            contador += 1

    return contador

texto_usuario = input("Digite um texto: ")
print(f"O texto digitado tem {contar_vogais(texto_usuario)} vogais.")
