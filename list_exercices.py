#Análise de Notas: Peça 5 notas. Calcule a média e informe quantas notas foram acima de 7.0
#Define o valor de 0 para atribuir o valor da nota anterior e somar depois
soma = 0
contador = 0

for n in range(1, 6):
    nota = float(input(f"Digite a {n}° nota: "))

    soma = soma + nota

    if nota >= 7:
        nota = contador
        contador = contador + 1

media = soma / 5

print(f"\nA média das notas foi {media}!")
print(f"Teve {contador} notas acima de 7.0!")




    