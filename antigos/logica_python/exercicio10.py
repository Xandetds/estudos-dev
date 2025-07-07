notas = []

for i in range (5):
    nota = float(input("Escreva cinco notas: "))
    notas.append(nota)


print(f"As notas digitadas são: {notas}")

media = sum(notas) / len(notas)

print(f"A média das notas digitadas é: {media:.1f}")

notas_acima_da_media = []

for nota in notas:
    if nota > media:
        notas_acima_da_media.append(nota)

print(f"As notas que passaram da média foram: {notas_acima_da_media}")

