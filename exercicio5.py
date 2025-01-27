numero = int(input("Digite um número para verificar se é primo: "))

primo = True

if numero < 2:
    primo = False
else:
    for i in range(2, numero):
        if numero % i == 0:
            primo = False
            break

if primo:
    print(f"{numero} é um número primo.")
else:
    print(f"{numero} não é um número primo.")
