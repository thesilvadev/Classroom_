#print("\n----------CALCULADORA DE IMC----------\n")

#height= float(input("Digite sua altura\nR: "))
#weight= float(input("Digite seu peso\nR: "))

#height= height**2
#height= f"{height:.2f}"
#height= float(height)


#imc= weight / height



#if imc <18.5:
#    print(f"Você está abaixo do peso!")
#elif imc >= 18.5 <= 24.9:
#    print(f"Você está no peso ideal!")
#elif imc >= 25:
#    print(f"Você está acima do peso!")
#------------------------------------------------------------------------------------------------

#print("\n----------CONVERSOR DE TEMPERATURA----------\n")

#temp= float(input("Digite uma temperatura em graus Celcius\nR: "))

#print(f"Você deseja converter essa temperatura em Fahrenheit? (s/n)")

#Calculo para converter de Celsius para Fahrenheit
#calc= temp*1.8 + 32

#resposta
#convert= input("R: ")


#if convert =="s":
#    print(f"A temperatura em Fahrenheit é {calc}°")
#elif convert =="n":
#    print(f"A temperatura em Celsius é {temp}°")

#--------------------------------------------------------------------------------------------------

#print("\n-----------ANÁLISE DE PRODUTO-----------\n")   
#
#product= float(input("Digite o preço do produto em R$\nR: "))
#
#if product <=50:
#    print("Este produto está barato!")
#elif product <100:
#    print("Este produto não está tão barato!")
#elif product >100:
#    print("Este produto está caro!")

#--------------------------------------------------------------------------------------------------

#print("\n-----------TURNO DE ESTUDO-----------\n")

#print("(m) Matutino, (v) Vespertino, (n) Noturno\n")

#turn= input("Em qual turno você estuda?\nR: ")

#if turn =="m":
#    print("Bom dia!")
#elif turn =="v":
#    print("Boa tarde!")
#elif turn =="n":
#    print("Boa noite!")
#else:
#   print("Desculpe, turno não reconhecido :( ")

#---------------------------------------------------------------------------------------------

#print("\n----------BEM VINDO----------\n")

#user= input("User: ")
#password= input("\nPassword: ")

#if user == "admin" and password =="fatec123":
#    print("\n----------ACESSO LIBERADO----------\n")
#else:
#    print("Sorry, you don't have permission to access :(")

#----------------------------------------------------------------------------------------------

#print("\n----------MONTANDO TRIÂNGULOS----------\n")

#print("      ^  ")
#print("     /_\     \n")

#print("Digite 3 numeros e veja se é possivel formar um triangulo com eles!\n")

#lado_1= float(input("Digite o primeiro número: "))
#lado_2= float(input("Digite o segundo número: "))
#lado_3= float(input("Digite o terceiro número: "))

#if (lado_1 < lado_2 + lado_3) and (lado_2 < lado_1 + lado_3) and (lado_3 < lado_1 + lado_2):
#    print("Parabéns! Você conseguiu montar um triângulo!")
#else:
#    print("Não foi dessa ves, continue tentando!")

#----------------------------------------------------------------------------------------------

#print("\n----------CAMPANHA VOTAÇÃO----------\n")

#age= int(input("Digite sua idade\nR: "))

#if age >=18 and age <=70:
#    print("Seu voto é obrigatório na campanha!")
#elif age >=16 <=17 or age >=71:
#    print("Seu voto é facultativo!")
#else:
#    print("Desculpe, você ainda não pode votar!")

#-----------------------------------------------------------------------------------------------

#print("\n----------CUPONOMIA----------\n")

#print("Para participar do desconto responda:\n")

#age= int(input("Digite sua idade: "))

#shop= float(input("\nDigite o valor total da compra: "))

#if age >=65 or shop >100:
#    print("Parabens! Você ganhou um desconto.")
#else:
#    print("Desculpe, você não pode participar do desconto.")

#-----------------------------------------------------------------------------

#print("\n----------ANO BISSEXTO----------\n")

#print("\nDigite um ano para verificar se é um ano bissexto!\n")

#ano= int(input("Digite um algum ano\nR: "))

#if ano % 4 or ano % 400:
#    print("Este ano é bissexto!")
#elif not ano % 100:
#    print("Tente novamente!")

#-----------------------------------------------------------------------------

#print("\n----------NUMERO SECRETO----------\n")

#num="s"

#print("tente acertar o numero secreto\n")

#while num =="s":
#    numero= int(input("DESCUBRA A SENHA! DIGITE UM NUMERO\nR: "))
#    if numero ==0:
#        print("Você encontrou o numero secreto!")
#        num= input("Deseja continuar? (s/n)\nR: ")
#    else:
#        print("voce errou! Tente novamente.")
#print("FIM DO PROGRAMA")

#------------------------------------------------------------------------------

#Login com Níveis: Peça o login. Se for "admin", peça a senha. Se a senha
#estiver correta, pergunte se quer "Reiniciar Sistema" ou "Desligar". Se o login
#não for "admin", diga "Acesso de Usuário Comum"

#while True:
#    print("\n----------LOGIN----------\n")
    
#    user= "admin"
#    senha= "170106"


#    login= input("\nNome de Usuário: ").lower().strip()


#    if login != user:
#        user_c= str(input("\nDigite a senha: "))
#        print("\nAcesso de Usuário Comum Concedida")
#
#        reiniciar= input("\nDeseja reiniciar o sistema? (s/n)\nR: ")
#        if reiniciar == "n":
#            print("FIM DO PROGRAMA")
#            break
#

#    else:
#        sen1= input("\nDigite a senha: ")
#       if sen1 == senha:
#            print("\nACESSO DE ADMINISTRADOR CONCEDIDA")
#            reiniciar= input("\nDeseja reiniciar o sistema? (s/n)\nR: ")
#            if reiniciar == "n":
#                print("FIM DO PROGRAMA")
#               break
#        else:   
#            ask2= input("\nSenha Incorreta! Tentar novamente? (s/n)\nR: ")
#            if ask2 == "n":
#                print()
#            while True:
#
#                if ask2 == "n":
#                    print("FIM DO PROGRAMA")
#                    break
#                elif ask2 == "s":
#                    sen2= input("\nDigite a senha: ")
#                    if sen2 == senha:
#                        print("\nACESSO DE ADMINISTRADOR CONCEDIDA\n")
#                       reiniciar= input("\nDeseja reiniciar o sistema? (s/n)\nR: \n")
#                        if reiniciar == "n":
#                            break
#                    else:
#                        ask2= input("\nSenha Incorreta! Tentar novamente? (s/n)\nR: ")
#
#----------------------------------------------------------------------------------------

#Clima e Vestimenta: Pergunte se está chovendo (S/N). Se sim, pergunte se está
#ventando forte (S/N). Se chover e ventar, diga "Use capa de chuva reforçada".
#Se apenas chover, "Use guarda-chuva". Se não chover, diga "Tenha um bom dia"


#print("\n-----CLIN ASSISTENTE METEREOLOGICO (×_×)-----\n")

#nome= input("Olá meu nome é Clin, assistente virtual de metereologia \(^o^)/\n\nPara te conhecer melhor, por favor digite seu nome: ")
#chovendo= input(f"\n É um prazer te ajudar {nome}! Me diz uma coisa, está chovendo hoje? (s/n)\nR: ")

#if chovendo =="s":
#    ventando= input("\nNossa...(ó﹏ò｡)\n\nE está ventando? (s/n)\nR: ")
#    if ventando == "s":
#        print("\n(｡Ó﹏Ò｡) !! USE A CAPA DE CHUVA REFORÇADAA")
#    elif ventando == "n":
#        print("\n(◠‿◠) Não esqueça do guarda-chuva!")
#else:
#    print("\nUfa! Tenha um bom dia! (⌐■_■) ")
#
#---------------------------------------------------------------------------------------   

#Simulador de Caixa Eletrônico: Peça o valor a ser sacado (inteiro).
#Verifique se o valor é múltiplo de 10 (únicas notas disponíveis). Se for,
#pergunte se o cliente aceita pagar uma taxa de R$ 2,00 caso o valor seja
#superior a R$ 500. Exiba o status final da operação]

#print("\n----------CAIXA ELETRONICO----------\n")

#saque= int(input("Digite o valor a ser sacado\nR: "))
#taxa= 2
#calc= saque + 2


#if saque % 10 == 0 and saque > 500:
#    taxa= input("Para efetuar o saque, deseja pagar a taxa de R$2,00?\nR: ")
#   if taxa == "s":
#        print(f"O saque total é R${calc}")
#else:
#    print(f"Saque efetuado R${saque}!")
#
# --------------------------------------------------------------------------------------
#Raízes de Equação de 2º Grau: Peça os coeficientes A, B e C. Calcule o
#Delta. Se Delta < 0, diga "Não há raízes reais". Se Delta == 0, calcule e
#mostre a única raiz. Se Delta > 0, mostre as duas raízes. (Use math.sqrt)
#import math

#print("\n------------RAIZES EQUAÇÃO DO 2° GRAU------------\n")


#print("\nCalcule a raiz da equação de 2° grau:\n")

#a= int(input("Coeficiente A: "))
#b= int(input("Coeficiente B: "))
#c= int(input("Coeficiente C: "))

#delta= b**2 - 4*a*c

#if delta <0:
#    print("Não há raízes reais")
#elif delta ==0:
#    x= -b / (2*a)
#   print(f"A unica raiz é: {x}")
#elif delta > 0:
#   x1 = (-b + math.sqrt(delta)) / (2*a)
#    x2 = (-b - math.sqrt(delta)) / (2*a)
#    print("Está equação possui 2 raizes: ")
#    print(f"x1 = {x1}")
#    print(f"x2 = {x2}")
#
#----------------------------------------------------------------------------------------

#Faça um programa que peça uma nota, entre zero e dez. Mostre uma mensagem caso o valor seja inválido e continue pedindo até que o usuário informe um valor válido.

#nota = float(input("Digite uma nota: "))

#while nota >10 or nota <0:
#   nota= float(input("Digite uma nota válida: "))
#    if nota <=10 and nota >=0:
#        print("Nota validada!")

#-----------------------------------------------------------------------------------------

#Faça um programa que leia um nome de usuário e a sua senha e não aceite a senha igual ao nome do usuário, mostrando uma mensagem de erro e voltando a pedir as informações.

#nome= input("Digite seu nome\nR: ")
#senha= input("Digite a senha\nR: ")


#while senha == nome:
#    print("\nErro, a senha não pode ser igual ao nome de usuario!\n")
#    nome = input("Digite o seu nome de usuario: ")
#    senha = input("Digite a sua senha: ")
    
#------------------------------------------------------------------------------------------

#Peça um número inteiro ao usuário e diga se ele é par ou impar:

#num= int(input("Digite um numero\nR: "))

#if num % 2 ==0:
#    print("Este número é par")
#else:
#    print("Este número é impar")

#-----------------------------------------------------------------------------------------    

#Peça a idade de uma pessoa e informe se ela é maior ou menor de idade:

#idade= int(input("Digite sua idade\nR: "))

#if idade >= 18:
#    print("Você é maior de idade!")
#else:
#    print("Você é de menor!")

#---------------------------------------------------------------------------------------

#Peça um número e informe se ele é:positivo, negativo ou zero

#num= float(input("Digite um número\nR: "))

#if num >0:
#    print("Este numero é positivo!")
#elif num ==0:
#    print("Este numero é zero!")
#else:
#    print("Este numero é negativo")

#--------------------------------------------------------------------------------------

#Peça a nota de um aluno e mostre: Aprovado, se a nota for maior ou igual a 6 Reprovado, caso contrário

#nota= float(input("Digite sua nota\nR: "))

#if nota >= 6:
#    print("Voce está aprovado!")
#else:
#    print("Você está reprovado!")

#------------------------------------------------------------------------------------------------    

#Peça dois números e informe:qual é o maior ou se eles são iguais

#num_1= int(input("Digite o primeiro numero\nR: "))
#num_2= int(input("Digite o segundo numero\nR: "))

#if num_1 > num_2:
#    print(f"O numero {num_1} é o maior")
#elif num_2 > num_1:
#   print(f"O numero {num_2} é o maior")
#else:
#    print("Os numeros são iguais!")

#-------------------------------------------------------------------------------------------------

#Peça uma nota de 0 a 10 e mostre o conceito:
#A → nota entre 9 e 10
#B → nota entre 7 e 8.9
#C → nota entre 5 e 6.9
#D → abaixo de 5

#nota= float(input("Digite sua nota\nR: "))

#if nota >=9 and nota <= 10:
#   print("Você tirou A")
#elif nota >=7 and nota <=8.9:
#    print("Você tirou B")
#elif nota >= 5 and nota <=6.9:
#   print("Você tirou C")
#else:
#    print("Você tirou D")

#------------------------------------------------------------------------------------------------

#Peça a idade de uma pessoa e classifique como:
#Criança → até 12 anos
#Adolescente → de 13 a 17
#Adulto → de 18 a 59
#Idoso → 60 ou mais
#while True:

#    idade= int(input("\nDigite a sua idade\nR: "))

#    if idade <=12:
#        print("Criança")
#    elif idade >=13 and idade <=17:
#        print("Adolescente")
#    elif idade >=18 and idade <=59:
#        print("Adulto")
#    else:
#        print("Idoso")

#------------------------------------------------------------------------------------------------

#Calculadora simples

#Peça:

#o primeiro número
#o segundo número
#e uma operação (+, -, *, /)

#print("------CALCULADORA SIMPLES-----")

#num1= int(input("Digite o primeiro número\nR: "))
#num2= int(input("Digite o segundo número\nR: "))

#while True:
#    operation= input("Digite a operação (+, -, *, /)\nR: ")

#    if operation == "+":
#        calc= num1 + num2
#        print(f"Resultado: {calc}")
#        break
#    elif operation == "-":
#        calc= num1 - num2
#        print(f"Resultado: {calc}")
#       break
#    elif operation == "*":
#        calc= num1 * num2
#        print(f"Resultado: {calc}")
#       break
#    elif operation == "/":
#        calc= num1 / num2
#        print(f"Resultado: {calc}")
#        break
#    else:
#        print("Operação inválida, tente outro operador!\n")
#
#------------------------------------------------------------------------------------

#Dia da semana Peça um número de 1 a 7 e mostre o dia correspondente:

#1 → Domingo
#2 → Segunda
#3 → Terça
#...
#7 → Sábado

#Se o número for inválido, mostre uma mensagem de erro.
#-------------------------------------------------------------------------------------------

# Até o Zero: Peça números ao usuário repetidamente. O programa só para quando ele digitar 0

#num= 0
#tentativa= input("Tente acertar o numero secreto\nR: ")

#while tentativa != num:
#        tentativa= int(input("Você errou, tente novamente!\nR: "))
#print("Parabéns! Você encontrou o número 0")
#--------------------------------------------------------------------------------------------

#Validação de Nota: Peça uma nota entre 0 e 10. Enquanto o valor for inválido, continue pedindo.


#nota= int(input("Digite uma nota entre 0 e 10\nR: "))

#if nota >= 0 and nota <=10:
#    print("Nota validada!")
#else:
#    while nota <0 or nota >10:
#        nota= int(input("Digite uma nota válida\nR: "))
#        if nota <=10 and nota >=0:
#            print("Nota validada!")
#
#----------------------------------------------------------------------------------------------

#Senha de Acesso: Crie um sistema que peça uma senha e só libere o acesso quando a senha "python123" for digitada.

#senha= "python123"
#tent= input("Digite a senha\nR: ")

#if tent == senha:
#   print("Acesso concedido!")

#while tent != senha:
#    tent= input("Senha incorreta, tente novamente!\nR: ")
#    if tent == senha:
#        print("Acesso concedido!")
#----------------------------------------------------------------------------------------------

# Soma Acumulada: Peça números ao usuário e vá somando-os. Pare quando a soma total ultrapassar 100

#num= int(input("Digite um numero: "))
#soma= num
#if num >100:
#    print(f"O numero {num} ultrapassou o limite de 100 e não pode continuar!")
#else:
#    while soma <100:      
#            num2= int(input("Digite outro numero: "))
#           soma= soma + num2
#            if soma >100:
#                print(f"O numero {soma} ultrapassou o limite de 100 e não pode continuar!")
#----------------------------------------------------------------------------------------------

#Menu de Calculadora: Exiba um menu: [1] Somar [2] Subtrair [0] Sair. 
# O programa deve repetir até o usuário escolher 0

#while True:
#    print("\n-----MENU CALCULADORA-----\n")

#    print("\nSomar [1]\nSubtrair [2]\nSair [0]\n")

#    menu= int(input("R: "))
#    if menu == 1:
#       print("\n----- SOMA SELECIONADA-----\n")
#        num1= int(input("Digite o primeiro numero: "))
#        num2= int(input("Digite o segundo numero: "))
#        soma = num1 + num2
#        print(f"\nResultado= {soma}\n")
#   elif menu == 2:
#        print("\n----- SUBTRAÇÃO SELECIONADA-----\n")
#        num1= int(input("Digite o primeiro numero: "))
#        num2= int(input("Digite o segundo numero: "))
#       subtrair= num1 - num2
#        print(f"\nResultado= {subtrair}")
#    else:
#        print("FIM DO PROGRAMA")
#        break
#
#----------------------------------------------------------------------------------------------------------

#Adivinhação Simples: Defina um número secreto. O usuário deve tentar adivinhar; o programa avisa se o chute foi alto ou baixo até ele acertar.

#print("\n----- TENTE ADIVINHAR O NUMERO SECRETO-----\n")

#secreto = 14
#num=""
#num= int(input("Digite um número de 0 a 100\nR: "))

#while num != secreto:

  #  if num >=0 and num <=10:
  #      num= int(input("Tente um numero mais alto!\nR: "))
  #  elif num >=11 and num <=13 or num >=15 and num <=19:
  #      num= int(input("Você está muito perto, tente de novo!\nR: "))
  #  elif num >=20 and num <50:
 #       num= int(input("Tente um numero mais baixo!\nR: "))
 #   elif num >=50 and num <=100:
#        num= int(input("Você está longe, tente um número mais baixo!\nR: "))
#    elif num >100:
#        num= int(input("Digite um número de 0 a 100\nR: "))
#else:
#    print(f"Você encontrou o número secreto! ({secreto})")
#
 #-----------------------------------------------------------------------------------------------------------------

#População de Bactérias: Uma colônia dobra a cada hora. Começando com 1 bactéria, em quantas horas ela ultrapassará 1.000.000?


#bacterias= 1
#horas= 0
#print(f"hora: {horas}")
#print(f"bacterias: {bacterias}\n")

#while bacterias <1000000:
#    horas= horas + 1
#    bacterias= bacterias *2
#    print(f"horas: {horas}")
#    print(f"bacterias: {bacterias}\n")
#
#------------------------------------------------------------------------------------------------------

#Média Indeterminada: Peça números ao usuário. Pare quando ele digitar
#um número negativo. Ao final, mostre a média dos números positivos digitados  
  
#soma = 0
#contador = 0

# Solicita o primeiro número
#num = int(input("Digite um número\nR: "))

# O laço continua enquanto o número for positivo ou zero
#while num >= 0:
   # soma += num
  #  contador += 1
 #   num = int(input("Digite outro número\nR: "))

# Verifica se algum número positivo foi digitado para evitar divisão por zero
#if contador > 0:
#    media = soma / contador
#    print(f"FIM DO PROGRAMA\nA média dos números positivos foi: {media}")
#else:
#    print("FIM DO PROGRAMA\nNenhum número positivo foi digitado.")

#------------------------------------------------------------------------------------------------

#Caixa Eletrônico (Saque): Peça um valor de saque e informe quantas
#notas de R$ 50,00 serão entregues (use apenas while e subtrações).

# Caixa Eletrônico
#quantidade_notas = 0

#valor = float(input("Digite um valor de saque (mínimo R$ 50)\nR: "))

# WHILE 1: Enquanto o valor for menor que 50, ele 'prende' o usuário aqui
#while valor < 50:
 #   print("Valor inválido para notas de R$ 50.")
 #   valor = float(input("Digite um valor maior ou igual a 50\nR: "))

# WHILE 2: Enquanto o valor for maior ou igual a 50, ele vai subtraindo
#while valor >= 50:
#    valor -= 50           # Subtração do montante
#    quantidade_notas += 1  # Soma no contador de notas

#print(f"Total de notas de R$ 50,00 entregues: {quantidade_notas}")
#print(f"Valor restante: R$ {valor}")
#--------------------------------------------------------------------------------------------------------

#Validação de Cadastro: Peça Nome (mínimo 3 letras), Idade (0-120) e
#Salário (>0). Repita o pedido para cada campo até que o dado seja válido

#nome = input("Digite seu nome\nR: ").lower().strip()

#while len(nome) <=3:
#   nome = input("Por favor, digite um nome com mais de 3 caracteres\nR: ").lower().strip()

#idade = int(input("Agora digite sua idade\nR: "))

#while idade <0 or idade > 120:
#    idade = int(input("Por favor, digite  uma idade de 0 a 120\nR: "))

#salario = float(input("Agora digite seu salário mensal\nR: "))

#while salario <0:
#    print("Por favor, coloque um salário acima de 0 reais")
#else:
#   print(f"\nCadastro realizado {nome}!\n")

#print("Fim do programa")
#
#-------------------------------------------------------------------------------------------------------------------

#Contagem Crescente: Imprima todos os números de 1 a 20.

#for n in range(1, 21):
#    print(n)
#
#------------------------------------------------------------------------------------------------------------------

#Números Ímpares: Imprima todos os números ímpares entre 1 e 50

#for n in range(1, 51):
#    if n %2 != 0:
#        print(n)
#        
#------------------------------------------------------------------------------------------------------------------

#Tabuada Customizada: Peça um número ao usuário e exiba a tabuada dele de 1 a 10.

#num = int(input("Digite um numero para vizualizar tabuada\nR: "))

#for i in range(1, 11):
#    t= i * num
#
#   print(f"{i} * {num} = {t}")


#-----------------------------------------------------------------------------------------------------------------------

#Somatório Simples: Calcule a soma de todos os números de 1 a 100

#soma = 0

#for i in range(1, 101):
#    soma += i 
#    print(soma)
#
#---------------------------------------------------------------------------------------------------------------------

#Média de Temperaturas: Peça ao usuário 7 temperaturas
#(uma para cada dia da semana) e exiba a média ao final.
#dias = ["Segunda-feira", "Terça-feira", "Quarta-feira", "Quinta-feira", "Sexta-feira", "Sábado", "Domingo"]

#soma = 0

#for dia in dias:
#   temp = int(input(f"\nDigite uma temperatura de {dia}: "))
#    soma += temp

#media = soma / 7

#print(f"\nA media da temperatura da semana é {media:.2f}")

#--------------------------------------------------------------------------------------------------------------------------

#Fatorial (Introdução): Calcule o fatorial de um número inteiro positivo digitado pelo usuário (ex: 5! = 120)

#numero = int(input("Digite um numero: "))
#contador = 1

#for n in range(1, numero +1):
#    contador = contador * n
    
#    print(f"{n}! = {contador}")

#---------------------------------------------------------------------------------------------------------------------------

#Análise de Notas: Peça 5 notas. Calcule a média e informe quantas notas foram acima de 7.0
#Define o valor de 0 para atribuir o valor da nota anterior e somar depois
#soma = 0
#contador = 0

#for n in range(1, 6):
#    nota = float(input(f"Digite a {n}° nota: "))

#    soma = soma + nota

#    if nota >= 7:
#        nota = contador
#        contador = contador + 1

#media = soma / 5

#print(f"\nA média das notas foi {media}!")
#print(f"Teve {contador} notas acima de 7.0!")

#--------------------------------------------------------------------------------------------------------------

#Escreva um código usando input e atribuindo o resultado a uma variável. Não esqueça de
#fazer o casting para um valor numérico corretamente. Escreva um comentário explicando o
#que foi feito e o porquê

#Aqui foi usado a string como imput.Pois iremos coletar o nome do usuario
#nome = input("Digite seu nome: ")

#Aqui foi usado o int no input. Atribuindo a variavel idade como um numero inteiro
#idade = int(input("Digite sua idade: "))

#Foi usado como float pois é um numero real, ou seja, um numero com virgula (casas decimais)
#dinheiro = float(input("Digite quantos reais você tem: R$"))

#O emprestimo foi atribuido o valor "True" 
#emprestimo = True

#----------------------------------------------------------------------------------------------------------------------------------------
#import random

  

#for numero in range(5):  

#    numero = random.randint(1, 6)  

#print(f"Dado: {numero}")  

  

  

  

#v1 Modifique o codigo para que ele jogue 2 dados por 10x seguidos  

  

#for rodada in range(10):  

#    dado1 = random.randint(1, 6)  

#    dado2 = random.randint(1, 6)  

#    print(f"Dado 1: {dado1}\nDado 2: {dado2}\n")  

#print("\n---FIM DO PROGRAMA---\n")  

  

#v2 Conte quantas vezes os dados deram numeros iguais : ex.. 2 2 , 6 6 etc...  

  

#contagem = 0  

  

#for rodada in range(10):  

#    dado1 = random.randint(1, 6)  

#   dado2 = random.randint(1, 6)  

#    if dado1 == dado2:  

#        contagem = contagem + 1  

         

#    print(f"Dado 1: {dado1}\nDado 2: {dado2}\n")  

#print(f"Os dados se repetiram {contagem} vezes")  

  

#print("\n---FIM DO PROGRAMA---\n")  

  

#------------------------------------------------------------------------------------------------------------------------
  

#contagem = 0  

  

#for rodada in range(10):  

#    dado1 = random.randint(1, 6)  

#    dado2 = random.randint(1, 6)  

#    if dado1 == dado2:  

#        contagem = contagem +1  

#        print(f"Dado 1: {dado1}\nDado 2: {dado2}")  

#        print("Dados iguais\n")  

#        break  

         

#    print(f"Dado 1: {dado1}\nDado 2: {dado2}\n")  

#print(f"Os dados se repetiram {contagem} vezes antes de parar")  

#print("\n---FIM DO PROGRAMA---\n")  

  
#------------------------------------------------------------------------------------------
 
#v3 Faça o programa parar de jogar os dados se for detectado "Dados iguais"  


import random  


#contagem = 0  

  

#for rodada in range(10):  

#    dado1 = random.randint(1, 6)  

#    dado2 = random.randint(1, 6)  

#    contagem = contagem +1  

#    if dado1 == dado2:  

#        print(f"Dado 1: {dado1}\nDado 2: {dado2}")  

#        print("Dados iguais\n")  

#        break  

         

#    print(f"Dado 1: {dado1}\nDado 2: {dado2}\n")  

#print(f"Os dados se repetiram {contagem} vezes antes de parar")  

#print("\n---FIM DO PROGRAMA---\n")  

#-------------------------------------------------------------------------------------------------------------------

#Jogo jokeyPô, pc contra player:

#print(f"\n----- JokeyPô -----\n")

#for rodada in range(1):

#    pc = random.randint(1, 3)

#    if pc == 1:
#        pc = "✊"
#    elif pc == 2:
#        pc = "✋"
#    elif pc == 3:
#        pc = "✌️"

#    player = int(input("Tente me vencer 🤖!\n\nPedra [1] Papel [2] Tesoura [3]\nR: "))

#    if player == 1:
#        player = "✊"
#    elif player == 2:
#        player = "✋"
#    elif player == 3:
#        player = "✌️"


#if pc == "✊" and player == "✊":
#    print(f"\nPlayer: {player} \nPc: {pc}\n\nEmpate!")
#elif pc == "✋" and player == "✋":
#    print(f"\nPlayer: {player} \nPc: {pc}\n\nEmpate!")
#elif pc == "✌️" and player == "✌️":
#    print(f"\nPlayer: {player} \nPc: {pc}\n\nEmpate!")



#if pc == "✊" and player == "✌️":
#    print(f"\nPlayer: {player} \nPc: {pc}\n\nO 🤖 venceu!")
#elif pc == "✋" and player == "✊":
#    print(f"\nPlayer: {player} \nPc: {pc}\n\nO 🤖 venceu!")
#elif pc == "✌️" and player == "✋":
#    print(f"\nPlayer: {player} \nPc: {pc}\n\nO 🤖 venceu!")



#if pc == "✌️" and player == "✊":
#    print(f"\nPlayer: {player} \nPc: {pc}\n\nO Player venceu!") 
#elif pc == "✊" and player == "✋":
#    print(f"\nPlayer: {player} \nPc: {pc}\n\nO Player venceu!") 
#elif pc == "✋" and player == "✌️":
#    print(f"\nPlayer: {player} \nPc: {pc}\n\nO Player venceu!") 
    
#print("\n----- FIM DO PROGRAMA -----\n")


#-----------------------------------------------------------------------------------------

#V 1.1 - Play again [s/n]

#print(f"\n----- JokeyPô -----\n") # Titulo do Jogo!

#play_again = "s" # Definindo o valor que sera atribuido no while

#while play_again == "s": # Definindo o laço de repetição do Play Again

#    for rodada in range(1): # Jogo tera apenas 1 rodada [range(1)]

#        pc = random.randint(1, 3) # Aqui é onde o Pc irá escolher entre: Pedra, Papel ou Tesoura (aleatoriamente)

#        if pc == 1:
#            pc = "✊" # Definindo como o numero 1 será representado no jogo
#        elif pc == 2:
#            pc = "✋" # Definindo como o numero 2 será representado no jogo
#        elif pc == 3:
#            pc = "✌️" # Definindo como o numero 3 será representado no jogo

#        player = int(input("\nTente me vencer 🤖!\n\nPedra [1] Papel [2] Tesoura [3]\nR: ")) # Aqui é onde o jogador vai escolher entre: Pedra, Papel ou Tesoura

#        if player == 1:
#            player = "✊" # Definindo como o numero 1 será representado no jogo
#        elif player == 2:
#            player = "✋" # Definindo como o numero 2 será representado no jogo
#        elif player == 3:
#            player = "✌️" # Definindo como o numero 3 será representado no jogo


#    if pc == "✊" and player == "✊":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nEmpate!")
#    elif pc == "✋" and player == "✋":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nEmpate!")
#    elif pc == "✌️" and player == "✌️":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nEmpate!")
# Usando comparações para definir empate do jogo!


#    if pc == "✊" and player == "✌️":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO 🤖 venceu!")
#    elif pc == "✋" and player == "✊":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO 🤖 venceu!")
#    elif pc == "✌️" and player == "✋":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO 🤖 venceu!")
# Usando comparação para definir o ganhador do Jogo (PC)


#    if pc == "✌️" and player == "✊":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO Player venceu!") 
#    elif pc == "✊" and player == "✋":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO Player venceu!") 
#   elif pc == "✋" and player == "✌️":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO Player venceu!") 
# Usando comparação para definir o ganhador do Jogo (PLAYER)    


#    print("\n----- FIM DA RODADA -----\n") # Final da rodada

#    play_again = input("\nDeseja jogar novamente? [s/n]\nR: ") # Variavel para reiniciar o Play Again
#
#    while play_again != "s": # Caso o player coloque qualquer caracter difirete de "s" ou "n"
#    
#        print("Por favor, digite uma opção valida!") # Mensagem de caracter invalido!
#        play_again = input("\nDeseja jogar novamente? [s/n]\nR: ") # variavel para voltar para o primeiro laço de repetição caso a resposta seja "s"

#       if play_again == "n": #Caso a resposta seja "n" o programa encerra
#            print("\n----- FIM DO PROGRAMA -----\n")
#            break # Break para interromper o laço!

#------------------------------------------------------------------------------------------------------
       
#V.3 - Implemente um placar!

#print(f"\n----- JokeyPô -----\n") # Titulo do Jogo!

#pc_venceu = 0
#player_v = 0


#play_again = "s" # Definindo o valor que sera atribuido no while

#while play_again == "s": # Definindo o laço de repetição do Play Again

#    for rodada in range(1): # Jogo tera apenas 1 rodada [range(1)]

#        pc = random.randint(1, 3) # Aqui é onde o Pc irá escolher entre: Pedra, Papel ou Tesoura (aleatoriamente)

#        if pc == 1:
#            pc = "✊" # Definindo como o numero 1 será representado no jogo
#        elif pc == 2:
#            pc = "✋" # Definindo como o numero 2 será representado no jogo
#        elif pc == 3:
#            pc = "✌️" # Definindo como o numero 3 será representado no jogo

#        player = int(input("\nTente me vencer 🤖!\n\nPedra [1] Papel [2] Tesoura [3]\nR: ")) # Aqui é onde o jogador vai escolher entre: Pedra, Papel ou Tesoura

#        while player <= 0 or player >= 4:
#            print("\nPor favor selecione uma das opções válidas!")
#            player = int(input("\nTente me vencer 🤖!\n\nPedra [1] Papel [2] Tesoura [3]\nR: "))#

#        if player == 1:
#            player = "✊" # Definindo como o numero 1 será representado no jogo
#        elif player == 2:
#            player = "✋" # Definindo como o numero 2 será representado no jogo
#        elif player == 3:
#            player = "✌️" # Definindo como o numero 3 será representado no jogo

#   
#    if pc == "✊" and player == "✊":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nEmpate!")
#        print(f"\nPlacar do jogo: [Empate]")
##   elif pc == "✋" and player == "✋":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nEmpate!")
#        print(f"\nPlacar do jogo: [Empate]")
#    elif pc == "✌️" and player == "✌️":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nEmpate!")
#        print(f"\nPlacar do jogo: [Empate]")

# Usando comparações para definir empate do jogo!

#    if pc == "✊" and player == "✌️":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO 🤖 venceu!")
#        pc_venceu = pc_venceu + 1
#        player_v = player_v
#        print(f"\nPlacar do jogo: {player_v}] x [{pc_venceu}]")
#    elif pc == "✋" and player == "✊":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO 🤖 venceu!")
#       pc_venceu = pc_venceu + 1
#        player_v = player_v
#        print(f"\nPlacar do jogo: [{player_v}] x [{pc_venceu}]")
#    elif pc == "✌️" and player == "✋":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO 🤖 venceu!")
#        pc_venceu = pc_venceu + 1
#        player_v = player_v
#        print(f"\nPlacar do jogo: [{player_v}] x [{pc_venceu}]")

# Usando comparação para definir o ganhador do Jogo (PC)
    
#    if pc == "✌️" and player == "✊":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO Player venceu!")
#        player_v = player_v + 1
#        pc_venceu = pc_venceu
#       print(f"\nPlacar do jogo: [{player_v}] x [{pc_venceu}]")
#    elif pc == "✊" and player == "✋":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO Player venceu!")
#        player_v = player_v + 1
#        pc_venceu = pc_venceu
#        print(f"\nPlacar do jogo: [{player_v}] x [{pc_venceu}]")
#   elif pc == "✋" and player == "✌️":
#        print(f"\nPlayer: {player} \nPc: {pc}\n\nO Player venceu!")
#        player_v = player_v + 1
#        pc_venceu = pc_venceu
#        print(f"\nPlacar do jogo: [{player_v}] x [{pc_venceu}]") 
           
# Usando comparação para definir o ganhador do Jogo (PLAYER)
 

#    print("\n----- FIM DA RODADA -----\n") # Final da rodada

#    play_again = input("\nDeseja jogar novamente? [s/n]\nR: ") # Variavel para reiniciar o Play Again

#    while play_again != "s": # Caso o player coloque qualquer caracter difirete de "s" ou "n"
    
#        print("Por favor, digite uma opção valida!") # Mensagem de caracter invalido!
#        play_again = input("\nDeseja jogar novamente? [s/n]\nR: ") # variavel para voltar para o primeiro laço de repetição caso a resposta seja "s"

#        if play_again == "n": #Caso a resposta seja "n" o programa encerra
#            print("\n----- FIM DO PROGRAMA -----\n")
#            break # Break para interromper o laço!       

#----------------------------------------------------------------------------------------------------

# Aprendendo listas:

# Exemplo:

#frutas = ["Maça", "Banana", "Caju"]
#frutas.sort()
#print(frutas)

# ------------------------------------------------------------

# Criação e Acesso: Crie uma lista com 5 nomes de cidades. Imprima apenas a primeira  e a última cidade da lista.

#cidades = ["Londrina", "Cambé", "Ibiporã", "Rolândia", "Curitiba"]

#print(cidades[0], cidades[-1])

#Alteração Manual: Dada a lsita numeros = [10, 20, 30, 40, 50], altere o valor do terceiro elemento para 100 e imprima a lista atualizada

#numeros = [10, 20, 30, 40, 50]

#numeros[2] = 100
#print(numeros)

# Uso da Tupla: Crie uma tupla com os meses do ano. Tente alterar o primeiro mes para "Janeiro Alterado" e observe o erro gerado pelo Python. Escreva em um comentário por que o erro ocorreu.

#meses = ("Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro")

# Erro: 'tuple' object does not support item assignment

# Explicação: O erro acontece porque a tupla não pode ser alterada

# Entrada Dinamica: Crie um programa que peça ao usuário 5 numeros, adicione -os em uma lsita usando .append() e, ao final, exiba a soma de todos os itens (use a função sum()).


#contagem = 0
#lista = []

#print("\nDigite 5 numeros na lista para fazer a soma\n")

#for corredor in range(5):

#    numero = int(input(f"Digite o {corredor+1}° numero: "))
#    lista.append(numero)

#soma = sum(lista)

#print(f"\nlista = {lista}")
#print(f"A soma da lista é = {soma}")

#print("\n----- FIM DO PROGRAMA -----\n")

#--------------------------------------------------------------------------------------

# Ordenação de nomes: Peça ao usuario nomes de convidados ate que ele digite ate que ele digite "fim". Guarde os nomes em uma lista, coloque-os em ordem alfabetica e exiba a lista final.

















