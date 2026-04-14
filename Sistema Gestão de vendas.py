print("\n------SISTEMA DE GESTÃO DE VENDAS MENSAIS------\n")


nome_gestor = input("\nDigite o nome do gestor: ")

mes_referencia = input("\nDigite o mês de referência: ").upper()

meses = ["JANEIRO", "FEVEREIRO", "MARÇO", "ABRIL", "MAIO", "JUNHO", "JULHO", "AGOSTO", "SETEMBRO"]

while mes_referencia != "JANEIRO" and mes_referencia != "FEVEREIRO":
    print("mês inválido!")
    mes_referencia = input("\nDigite o mês de referência: ").upper()
else:
    dias_venda = int(input(f"\nQuantos dias de venda serão registrados em {mes_referencia}: "))


for d in range(1, dias_venda+1):

    valor_vendido = float(input(f"\nDigite o valor vendido do {d}° dia : "))
    



