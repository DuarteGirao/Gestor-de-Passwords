# 🔐 Gestor de Passwords

Um gestor de passwords seguro com interface web moderna, desenvolvido com Flask e MariaDB.

## 📋 Funcionalidades

- ✅ Adicionar passwords cifradas
- ✅ Ver passwords guardadas
- ✅ Proteção com password mestra
- ✅ Cifração segura (Fernet)
- ✅ Interface web moderna e responsiva

## 🚀 Instalação

1. **Criar ambiente virtual:**
```powershell
python -m venv .venv
.venv\Scripts\Activate
```

2. **Instalar dependências:**
```powershell
pip install flask python-dotenv cryptography mariadb
```

3. **Configurar ficheiro `.env`:**
```
master_password=SuaPasswordMestra
chave=SuaChaveFernet
```

4. **Criar base de dados MariaDB:**
```sql
CREATE DATABASE Projeto;
USE Projeto;
CREATE TABLE dados (
    id INT AUTO_INCREMENT PRIMARY KEY,
    Site VARCHAR(255),
    Utilizador VARCHAR(255),
    Password TEXT
);
```

## ▶️ Execução

```powershell
python main.py
```

Aceda a: `http://127.0.0.1:5000`

## 📁 Estrutura

```
├── main.py          # Aplicação Flask
├── auth.py          # Cifração/decifração
├── storage.py       # Base de dados
├── templates/       # Páginas HTML
│   ├── index.html
│   ├── adicionar.html
│   └── ver.html
└── static/          # CSS
    └── style.css
```

## 🔒 Segurança

- Passwords cifradas com Fernet (symmetric encryption)
- Password mestra para acesso às passwords
- Dados guardados de forma segura na base de dados

---
Desenvolvido em Python + Flask 🐍