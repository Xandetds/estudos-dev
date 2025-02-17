lista = []

while True:
    numero = input("Digite um número (ou 'sair' para parar): ")
    if numero.lower() == "sair":
        break
    lista.append(int(numero))



def calcular_media(lista):
    soma = 0

    for num in lista:
        soma += num

    quantidade = len(lista)
    media = soma / quantidade

    return media

if len(lista) > 0:
    print(f"A média dos números digitados é de: {calcular_media(lista)}")
else:
    print("Nenhum número foi digitado, não é possível calcular a média.")
