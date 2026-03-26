with open("exemplo.txt", "w") as f:
    f.write("Primeira linha\n")
    f.write("Segunda linha\n")
    f.write("Terceira linha\n")

linhas = []
with open("exemplo.txt", "r") as f:
    for linha in f:
        linhas.append(linha.strip())

print("Linhas do arquivo:", linhas)
