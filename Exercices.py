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
print("\n----------LOGIN----------\n")
    
sen2= "170106"
user= "admin"
senha= "170106"

login= input("Nome de Usuário: ").lower().strip()


if login != user:
    print("Acesso de Usuário Comum")

else:
    sen1= input("\nDigite a senha: ")
    if sen1 == senha:
        print("\nACESSO DE ADMINISTRADOR CONCEDIDA")
    else:
        while True:   
            ask2= input("\nSenha Incorreta! Tentar novamente? (s/n)\nR: ")

            if ask2 == "n":
                print("FIM DO PROGRAMA")
                break
            elif ask2 == "s":
                sen2= input("\nDigite a senha: ")
                if sen2 == senha:
                    print("\nACESSO DE ADMINISTRADOR CONCEDIDA")
                    break
