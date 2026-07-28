from cryptography.fernet import Fernet

KEY = Fernet.generate_key()

cipher = Fernet(KEY)

def encrypt(text):

    return cipher.encrypt(text.encode())

def decrypt(data):

    return cipher.decrypt(data).decode()
