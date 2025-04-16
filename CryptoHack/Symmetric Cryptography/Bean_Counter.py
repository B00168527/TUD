import requests
from Crypto.Util.strxor import strxor

# Call the encrypt_flag function from the endpoint and return the ciphertext value from the JSON
def encrypt():
    # Get the response from the endpoint
    response = requests.get("http://aes.cryptohack.org/bean_counter/encrypt/").json()
    # Get the encrypted value
    encrypted = response["encrypted"]
    return encrypted

# The 16 bytes of PNG file headers
png_header_bytes = bytes([0x89, 0x50, 0x4e, 0x47, 0x0d, 0x0a, 0x1a, 0x0a, 0x00, 0x00, 0x00, 0x0d, 0x49, 0x48, 0x44, 0x52])

# Call the endpoint and get the encrypted value
encrypted = bytes.fromhex(encrypt())

# XOR the PNG header bytes with the encrypted first block
keystream = strxor(encrypted[:len(png_header_bytes)], png_header_bytes)

# XOR the encrypted file with the repeated keystream
decrypted = bytes(x ^ y for x, y in zip(encrypted, keystream * (len(encrypted) // len(keystream))))

# Write the decrypted file to an file named "image.png"
with open('image.png', 'wb') as file:
        file.write(decrypted)
