import os
import auth, storage, chave

clear = lambda: os.system('cls') 

def MenuPrincipal():
    clear()
    print("----Menu Principal----")
    print("Opção 1: Adcionar Password")
    print("Opção 2: Ver Passwords")
    print("Opção 3: Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def MenuAdicionarPassword():
    clear()
    print("----Adicionar Password----")
    site = input("Digite o nome do site: ")
    username = input("Digite o nome de utilizador: ")
    password = input("Digite a password: ")
    return site, username, password

def MenuVerPasswords():
    clear()
    print("----Ver Passwords----")
    master_password = input("Digite a password mestra: ")
    if master_password != chave.master_password:
        print("Password mestra incorreta!")
        input("\nPressione Enter para continuar...")
        return None
    clear()
    site = input("Digite o nome do site para ver as passwords: ")
    return site

def MenuSair():
    print("A sair do programa. Até logo!")
    exit()

def MenuErro():
    print("Opção inválida. Por favor, tente novamente.")
    return

if __name__ == "__main__":
    while True:
        escolha = MenuPrincipal()
        if escolha == "1":
            site, username, password = MenuAdicionarPassword()
            storage.InserirDados(site, username, auth.cifrar_password(password))
        elif escolha == "2":
            site = MenuVerPasswords()
            if site is not None:
                storage.verPasswords(site)
                input("\nPressione Enter para continuar...")
        elif escolha == "3":
            MenuSair()
        else:
            MenuErro()
