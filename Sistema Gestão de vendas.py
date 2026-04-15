print("\n------SISTEMA DE GESTÃO DE VENDAS MENSAIS------\n")


nome_gestor = input("\nDigite o nome do gestor: ").capitalize()

mes_referencia = input("\nDigite o mês de referência: ").upper()

while mes_referencia != "JANEIRO" and "FEVEREIRO" and "MARÇO":#mes_referencia #!= "FEVEREIRO" and mes_referencia != "MARÇO" and mes_referencia != "ABRIL" and mes_referencia !=  "MAIO" and mes_referencia != :
    print("mês inválido!")
    mes_referencia = input("\nDigite o mês de referência: ").upper()
else:
    dias_venda = int(input(f"\nQuantos dias de venda serão registrados em {mes_referencia}: "))


for d in range(1, dias_venda+1):

    valor_vendido = float(input(f"\nDigite o valor vendido do {d}° dia : "))
    



