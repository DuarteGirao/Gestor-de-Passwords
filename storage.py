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
        """Insere uma nova password na base de dados"""
        try:
            cur.execute("INSERT INTO dados (Site, Utilizador, Password) VALUES (%s, %s, %s)", 
                        (site, utilizador, password))
            conn.commit()
        except mariadb.Error as e:
            print(f"Erro ao inserir: {e}")
            return False
        return True

    def verPasswords(site):
        """Obtém todas as passwords de um site específico"""
        try:
            import auth
            cur.execute("SELECT Site, Utilizador, Password FROM dados WHERE Site = %s", (site,))
            resultados = cur.fetchall()
            
            if resultados:
                passwords_list = []
                for resultado in resultados:
                    password_decifrada = auth.decifrar_password(resultado[2])
                    passwords_list.append({
                        "site": resultado[0],
                        "username": resultado[1],
                        "password": password_decifrada
                    })
                return passwords_list
            else:
                return []
        except mariadb.Error as e:
            print(f"Erro ao buscar dados: {e}")
            return None
    
except mariadb.Error as e:
    print(f"Erro na ligação à base de dados: {e}")
    sys.exit(1)