import json
import base64
from Crypto.Cipher import AES
from Crypto.Util.Padding import unpad

aes_key = b'CU\xc3>\x0f\xe7*}"\xd9 x\x11V\x9d\x1e"Q~S\xd6.\xa7\x0f\x8b\x10w\x8aw\xb7\xba\xb7'

def decrypt_data(encrypted_data, key):
    # Decode the base64-encoded encrypted data
    encrypted_data_bytes = base64.b64decode(encrypted_data)

    # Extract the Initialization Vector (IV) and the actual encrypted data
    iv = encrypted_data_bytes[:AES.block_size]
    ciphertext = encrypted_data_bytes[AES.block_size:]

    # Create a new AES cipher object using the key and IV
    cipher = AES.new(key, AES.MODE_CBC, iv)

    # Decrypt the ciphertext
    decrypted_padded_data = cipher.decrypt(ciphertext)

    # Remove padding to get the original data
    decrypted_data_bytes = unpad(decrypted_padded_data, AES.block_size)

    # Convert bytes back to the original data format (JSON)
    decrypted_data = json.loads(decrypted_data_bytes.decode('utf-8'))

    return decrypted_data

# Example usage:
# key = PBKDF2("password", salt, dkLen=32)  # Generate the same key used in encryption
# encrypted = encrypt_data({"example": "data"}, key)
# decrypted = decrypt_data(encrypted, key)
# print(decrypted)
