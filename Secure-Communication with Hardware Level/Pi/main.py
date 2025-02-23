import read_arduino
import encrypt
import send_data
from Crypto.Random import get_random_bytes

def main():
    counter = 1
    aes_key = b'CU\xc3>\x0f\xe7*}"\xd9 x\x11V\x9d\x1e"Q~S\xd6.\xa7\x0f\x8b\x10w\x8aw\xb7\xba\xb7'
    
    while counter <= 5:
        print("Reading data from arduino for " + str(counter) + " times")
        counter = counter + 1
        data = read_arduino.read_arduino_data()
        encrypted_data = encrypt.encrypt_data(data,aes_key)
        print("Encrypted data: " + encrypted_data)
        send_data.send_data_to_api(encrypted_data)
        print("\n\n")
if __name__ == "__main__":
    main()