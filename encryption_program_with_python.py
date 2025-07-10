import random
import string

chars =  " " + string.punctuation + string.ascii_letters + string.digits
chars = list(chars)
key = chars.copy()

random.shuffle(key)

# print(f"chars: {chars}")
# print(f"key: {key}")

print("Encryption function")

plain_text = input("Enter the text to encrypt: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original text: {plain_text}")
print(f"cipher text: {cipher_text}")


print("Decryption function")

cipher_text = input("Enter the text to decrypt: ")
plain_text = ""

for letter in cipher_text:
    index = key.index(letter)
    plain_text += chars[index]


print(f"cipher text: {cipher_text}")
print(f"original text: {plain_text}")

