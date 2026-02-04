import mariadb
import sys

try:
    conn = mariadb.connect(
        user="root",
        password="",
        host="127.0.0.1",
        port=3306,
        database="Projeto"
    )
    
    cur = conn.cursor()
    
    def InserirDados(site, utilizador, password):
        try:
            cur.execute("INSERT INTO dados (Site, Utilizador, Password) VALUES (%s, %s, %s)", 
                        (site, utilizador, password))
            conn.commit()
            print("Inserção feita!")
        except mariadb.Error as e:
            print(f"Erro ao inserir: {e}")

    def verPasswords(site):
        try:
            import auth
            cur.execute("SELECT Site, Utilizador, Password FROM dados WHERE Site = %s", (site,))
            resultados = cur.fetchall()
            if resultados:
                for resultado in resultados:
                    password_decifrada = auth.decifrar_password(resultado[2])
                    print(f"Site: {resultado[0]}, Utilizador: {resultado[1]}, Password: {password_decifrada}")
            else:
                print("Nenhum dado encontrado para o site fornecido.")
        except mariadb.Error as e:
            print(f"Erro ao buscar dados: {e}")
    
except mariadb.Error as e:
    print(f"Erro: {e}")
    sys.exit(1)