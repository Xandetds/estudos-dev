produtos = {}

for i in range(3):
    nome_produto = input("Digite o nome do produto que você deseja adicionar: ")
    preco_produto = float(input("Digite o preço do produto que você deseja adicionar: "))
    produtos[nome_produto] = preco_produto

print(produtos)

pesquisa = input("Digite o nome do produto que voce quer pesquisar: ")

if pesquisa in produtos:
    print(f"O preço do produto '{pesquisa}' é R${produtos[pesquisa]:.2f}")
else:
    print("O produto digitado nao está no catálogo")