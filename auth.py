import argon2

ph = argon2.PasswordHasher()

def hash_password(password: str) -> str:
    return ph.hash(password)
