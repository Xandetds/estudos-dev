alunos = []
soma = 0
for i in range(5):
    nome = input(f"Digite o nome do aluno {i+1}: ")
    nota = float(input(f"Digite a nota de {nome}: "))
    alunos.append((nome, nota))
    soma += nota

media = soma / 5

print(f"A média é igual a: {media:.1f}")
print("\nAlunos com nota acima da média:")
for aluno in alunos:
    nome, nota = aluno
    if nota > media:
        print(f"{nome}: {nota}")

# Alteração mínima para commit
