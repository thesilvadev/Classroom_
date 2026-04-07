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

nome= input("Digite seu nome: ")

if nome == "   ":
    print("Por favor, digite um nome com mais de 3 caracteres")