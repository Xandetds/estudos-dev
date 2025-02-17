contatos = {}

for i in range(3):
    nome_contato = input("Digite o nome do contato que você deseja adicionar: ")
    numero_contato = int(input("Digite o número do contato que você deseja adicionar: "))
    contatos[nome_contato] = numero_contato

print(contatos)

pesquisa = input("Digite o nome do contato que voce quer pesquisar: ")

if pesquisa in contatos:
    print(f"O numero do contato '{pesquisa}' é: {contatos[pesquisa]}")
else:
    print("O contato digitado nao está na lista de contatos")