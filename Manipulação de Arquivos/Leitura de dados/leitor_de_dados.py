with open(pasta_dados, 'a', encoding="utf-8") as d: 
    #Nome
    nome = input("Digite seu nome: ")
    d.write(f"Nome: {nome}\n")
    #RG
    while True:
        rg = input("Digite seu RG (12.345.678-9): ")
        rg_limpo = rg.replace(".", "").replace("-", "")
        if rg_limpo.isnumeric() and len(rg) == 12:
            d.write(f"RG: {rg_limpo}\n")
            break
        else:
            print("Número inválido, digite novamente!")
    #RG
    while True:
        cpf = input("Digite seu CPF (123.456.789-0): ")
        cpf_limpo = rg.replace(".", "").replace("-", "")
        if cpf_limpo.isnumeric() and len(cpf) == 14:
            d.write(f"CPF: {cpf_limpo}\n")
            break
        else:
            print("Número inválido, digite novamente!")
    #Idade
    nascimento = input("Digite sua data de nascimento (dd/mm/aaaa): ")
    d.write(f"Data de Nascimento: {nascimento}\n")
    #Definindo dia, mês e ano
    dia, mes, ano = nascimento.split("/")
    dia = int(dia)
    mes = int(mes)
    ano = int(ano)
    dia_atual = 23
    mes_atual = 3
    ano_atual = 2026
    #Definindo e calculando a idade
    idade = ano_atual - ano
    if (mes_atual, dia_atual) < (mes, dia):
        idade -= 1
    d.write(f"Idade: {idade}")
    d.write(f"\n------------------------------------------------\n")
    d.close()
