print("\n------SISTEMA DE GESTÃO DE VENDAS MENSAIS------\n")


nome_gestor = input("\nDigite o nome do gestor: ").capitalize()

mes = input("\nDigite o mês de referência: ").upper()

while mes != "JANEIRO" and  mes != "FEVEREIRO" and mes != "MARÇO" and  mes != "ABRIL" and  mes != "MAIO" and  mes != "JUNHO" and  mes != "JULHO" and  mes != "AGOSTO" and  mes != "SETEMBRO" and  mes != "OUTUBRO" and  mes != "NOVEMBRO" and  mes != "DEZEMBRO":
    print("mês inválido!")
    mes = input("\nDigite o mês de referência: ").upper()
else:
    dias_venda = int(input(f"\nQuantos dias de venda serão registrados em {mes}: "))

soma = 0

for d in range(1, dias_venda+1):

    valor_vendido = float(input(f"\nDigite o valor vendido do {d}° dia : R$"))

    soma = soma + valor_vendido

print(f"A soma das vendas do mes de {mes} é de R${soma:.2f}")
    



