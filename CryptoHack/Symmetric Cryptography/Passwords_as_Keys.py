from Crypto.Cipher import AES
import hashlib
import random
import codecs


def decrypt(ciphertext, password_hash):
    ciphertext = bytes.fromhex(ciphertext)
    key = bytes.fromhex(password_hash)

    cipher = AES.new(key, AES.MODE_ECB)
    try:
        decrypted = cipher.decrypt(ciphertext)
    except ValueError as e:
        return {"error": str(e)}

    return {"plaintext": decrypted.hex()}


ciphertext = "c92b7734070205bdf6c0087a751466ec13ae15e6f1bcdd3f3a535ec0f4bbae66"

# Get the words from the file
with open("words.txt") as f:
    words = [w.strip() for w in f.readlines()]

for word in words:
    wordHashed = hashlib.md5(word.encode()).hexdigest()

    hextext = decrypt(ciphertext, wordHashed)
    try:
        plaintext = codecs.decode(hextext['plaintext'],'hex').decode('ascii')
        print(word)
        print(plaintext)
        break
    except:
        continue
