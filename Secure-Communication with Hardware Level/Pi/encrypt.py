import json
import base64
from Crypto.Cipher import AES
from Crypto.Protocol.KDF import PBKDF2
from Crypto.Util.Padding import pad
from Crypto.Random import get_random_bytes
import time

def encrypt_data(data, key):
    cipher = AES.new(key, AES.MODE_CBC)

    # Convert the data to bytes (UTF-8)
    data_bytes = json.dumps(data).encode('utf-8')

    # Pad the data to be a multiple of 16 bytes (block size of AES)
    padded_data = pad(data_bytes, AES.block_size)

    # Encrypt the data
    encrypted_data = cipher.encrypt(padded_data)

    # Return the encrypted data along with the initialization vector (IV)
    # Both are needed to decrypt the data later
    return base64.b64encode(cipher.iv + encrypted_data).decode('utf-8')


