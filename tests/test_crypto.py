from src.crypto import encrypt, decrypt

def test_crypto():

    text = "secret"

    assert decrypt(encrypt(text)) == text
