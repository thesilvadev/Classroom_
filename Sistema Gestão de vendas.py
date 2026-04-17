start = "s"

while start == "s":


    print("\n------SISTEMA DE GESTÃO DE VENDAS MENSAIS------\n")

    total_vendido = 0
    maior_venda = 0
    menor_venda = 9999999


    nome_gestor = input("\nDigite o nome do gestor: ").capitalize()

    mes = input("\nDigite o mês de referência: ").upper()

    while mes != "JANEIRO" and  mes != "FEVEREIRO" and mes != "MARÇO" and  mes != "ABRIL" and  mes != "MAIO" and  mes != "JUNHO" and  mes != "JULHO" and  mes != "AGOSTO" and  mes != "SETEMBRO" and  mes != "OUTUBRO" and  mes != "NOVEMBRO" and  mes != "DEZEMBRO":
        print("mês inválido!")
        mes = input("\nDigite o mês de referência: ").upper()
    else:
        dias_venda = int(input(f"\nQuantos dias de venda serão registrados em {mes}: "))

    while dias_venda >= 32: 

        dias_venda = int(input(f"\nPor favor, digite um dia válido para o mes de {mes}: "))

    else:
        for dia in range(1, dias_venda+1):

            valor = float(input(f"\nDigite o valor vendido do {dia}° dia : R$"))              

            total_vendido = total_vendido + valor
        
            if valor > maior_venda:
                maior_venda = valor

            if valor < menor_venda:
                menor_venda = valor
        



    media = total_vendido / dias_venda


    sem_venda = 31 - dias_venda


    if total_vendido <10000:
        meta_mensal = "Não atingida"
    else:
        meta_mensal = "Atingida!"

    if total_vendido < 8500:
        aproveitamento = "Aproveitamento Regular"
    elif total_vendido >= 8500 and total_vendido <= 10000:
        aproveitamento = "Aproveitamento Bom"
    elif total_vendido >10000 and total_vendido <12500:
        aproveitamento = "Aproveitamento Ótimo"
    elif total_vendido > 12500:
        aproveitamento = "Aproveitamento Excelente"


    print(f"\n========== RELATÓRIO DE VENDAS ==========\n")
    print(f"Gestor: {nome_gestor}\n")
    print(f"Mês: {mes}\n")
    print(f"\nDias com vendas neste mês: {dias_venda} dias")
    print(f"\nTotal vendido no período: R$ {total_vendido:.2f}")
    print(f"\nMédia de vendas diárias: R$ {media:.2f}")
    print(f"\nMeta mensal: {meta_mensal}")
    print(f"\nMaior venda do período: R$ {maior_venda:.2f}")
    print(f"\nMenor venda do período: R$ {menor_venda:.2f}")
    print(f"\nDias sem venda: {sem_venda} dias")
    print(f"\nAproveitamento meta mensal: {aproveitamento}")
    print(f"\n========== FIM DO RELATÓRIO ==========\n")

    start = input("\n\nDeseja refazer o relatório? (s/n)\nR: ")

    if start != "s":
        print("FIM DO PROGRAMA")








    



