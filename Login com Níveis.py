#Login com Níveis: Peça o login. Se for "admin", peça a senha. Se a senha
#estiver correta, pergunte se quer "Reiniciar Sistema" ou "Desligar". Se o login
#não for "admin", diga "Acesso de Usuário Comum"

while True:
    print("\n----------LOGIN----------\n")
    
    user= "admin"
    senha= "170106"


    login= input("\nNome de Usuário: ").lower().strip()


    if login != user:
        user_c= str(input("\nDigite a senha: "))
        print("\nAcesso de Usuário Comum Concedida")

        reiniciar= input("\nDeseja reiniciar o sistema? (s/n)\nR: ")
        if reiniciar == "n":
            print("FIM DO PROGRAMA")
            break


    else:
        sen1= input("\nDigite a senha: ")
        if sen1 == senha:
            print("\nACESSO DE ADMINISTRADOR CONCEDIDA")
            reiniciar= input("\nDeseja reiniciar o sistema? (s/n)\nR: ")
            if reiniciar == "n":
                print("FIM DO PROGRAMA")
                break
        else:   
            ask2= input("\nSenha Incorreta! Tentar novamente? (s/n)\nR: ")
            if ask2 == "n":
                print()
            while True:

                if ask2 == "n":
                    print("FIM DO PROGRAMA")
                    break
                elif ask2 == "s":
                    sen2= input("\nDigite a senha: ")
                    if sen2 == senha:
                        print("\nACESSO DE ADMINISTRADOR CONCEDIDA\n")
                        reiniciar= input("\nDeseja reiniciar o sistema? (s/n)\nR: \n")
                        if reiniciar == "n":
                            break
                    else:
                        ask2= input("\nSenha Incorreta! Tentar novamente? (s/n)\nR: ")