from cryptography.fernet import Fernet
import chave

cipher = Fernet(chave.chave)

def cifrar_password(password: str) -> str:
    """Cifra a password para guardar na BD"""
    return cipher.encrypt(password.encode()).decode()

def decifrar_password(password_cifrada: str) -> str:
    """Decifra a password para mostrar"""
    return cipher.decrypt(password_cifrada.encode()).decode()
