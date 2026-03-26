from datetime import date

nome = input("Nome: ")
rg = input("RG: ")
cpf = input("CPF: ")
ano_nasc = int(input("Ano de nascimento: "))

idade = date.today().year - ano_nasc

with open("dados_pessoa.txt", "w") as f:
    f.write(f"Nome: {nome}\n")
    f.write(f"RG: {rg}\n")
    f.write(f"CPF: {cpf}\n")
    f.write(f"Ano de Nascimento: {ano_nasc}\n")
    f.write(f"Idade: {idade} anos\n")

print("Arquivo 'dados_pessoa.txt' criado!")
