import auth, storage
from auth import ph

def MenuPrincipal():
    print("----Menu Principal----")
    print("Opção 1: Adcionar Password")
    print("Opção 2: Ver Passwords")
    print("Opção 3: Sair")
    escolha = input("Escolha uma opção: ")
    return escolha

def MenuAdicionarPassword():
    print("----Adicionar Password----")
    site = input("Digite o nome do site: ")
    username = input("Digite o nome de utilizador: ")
    password = input("Digite a password: ")
    return site, username, password

def MenuVerPasswords():
    print("----Ver Passwords----")
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
            storage.pytojson(site, username, ph.hash(password))
        elif escolha == "2":
            site = MenuVerPasswords()
            storage.verPasswords(site)
        elif escolha == "3":
            MenuSair()
        else:
            MenuErro()
