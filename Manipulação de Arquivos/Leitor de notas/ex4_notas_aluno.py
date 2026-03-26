nome = input("Nome do aluno: ")
nota1 = float(input("Nota 1: "))
nota2 = float(input("Nota 2: "))

media = (nota1 + nota2) / 2
situacao = "Aprovado" if media >= 6 else "Reprovado"

with open("resultado_aluno.txt", "w") as f:
    f.write(f"Nome: {nome}\n")
    f.write(f"Nota 1: {nota1}\n")
    f.write(f"Nota 2: {nota2}\n")
    f.write(f"Média Final: {media:.2f}\n")
    f.write(f"Situação: {situacao}\n")

print(f"{nome} - Média: {media:.2f} - {situacao}")
