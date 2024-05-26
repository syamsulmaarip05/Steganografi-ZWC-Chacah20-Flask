# chacha.py

from Crypto.Cipher import ChaCha20
from Crypto.Random import get_random_bytes
import binascii
import hashlib

def get_private_key(password):
    return hashlib.sha256(password.encode('utf-8')).digest()

def encrypt(passwrd, message):
    key = get_private_key(passwrd)
    nonce = get_random_bytes(8)
    cipher = ChaCha20.new(key=key, nonce=nonce)
    ciphertext = cipher.encrypt(message.encode('utf-8'))
    return binascii.hexlify(cipher.nonce + ciphertext).decode('utf-8')

def decrypt(passwrd, message):
    try:
        key = get_private_key(passwrd)
        ciphertext = binascii.unhexlify(message.encode('utf-8'))
        nonce = ciphertext[:8]
        ciphertext = ciphertext[8:]
        cipher = ChaCha20.new(key=key, nonce=nonce)
        plaintext = cipher.decrypt(ciphertext).decode('utf-8')
        return plaintext
    except ValueError:
        return "Tidak ada pesan"
