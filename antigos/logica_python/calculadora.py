valor_1 = float(input("adicione um valor"))
valor_2 = float(input("adicione outro valor"))
operacao = input

print("Escolha uma operação matemática:")
print("1 - Soma (+)")
print("2 - Subtração (-)")
print("3 - Multiplicação (*)")
print("4 - Divisão (/)")
print("5 - Potência (**")
opcao = input("Digite o número da operação desejada: ")

if opcao == "1":
    print(valor_1 + valor_2)
elif opcao == "2":
    print(valor_1 - valor_2)
elif opcao == "3":
    print(valor_1 * valor_2)
elif opcao == "4":
    print(valor_1 / valor_2)
elif opcao == "5":
    print(valor_1 ** valor_2)
else:
    print("Opção inválida!")


