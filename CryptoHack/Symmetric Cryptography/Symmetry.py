import requests
from Crypto.Util.strxor import strxor

# Call the encrypt_flag function from the endpoint and return the ciphertext value from the JSON
def encrypt_flag():
    # Get the response from the endpoint
    response = requests.get("http://aes.cryptohack.org/symmetry/encrypt_flag/").json()
    # Get the ciphertext value
    ciphertext = response["ciphertext"]
    return ciphertext

# Call the encrypt function from the endpoint and return the ciphertext value from the JSON
def encrypt(plaintext, iv):
    encrypt_endpoint = f"http://aes.cryptohack.org/symmetry/encrypt/{{}}/{{}}/"

    # Get the response from the endpoint
    response = requests.get(encrypt_endpoint.format(plaintext, iv)).json()
    # Get the ciphertext value
    ciphertext = response["ciphertext"]
    return ciphertext

# Get the encrypted flag
flag_ciphertext_hex = encrypt_flag()

# Extract the IV (first 16 bytes)
iv_hex = flag_ciphertext_hex[:32]
# Extract the first block of ciphertext
first_block_ciphertext_hex = flag_ciphertext_hex[32:64]
# Extract the second block of ciphertext
second_block_ciphertext_hex = flag_ciphertext_hex[64:96]

# Create 16 bytes of known plaintext (zeros)
known_plaintext_hex = "00" * 16

# Encrypt known plaintext with IV to get first keystream block
keystream_hex_1 = encrypt(known_plaintext_hex, iv_hex)
keystream_1 = bytes.fromhex(keystream_hex_1)

# XOR the keystream and first ciphertext block to recover first plaintext block
first_block_ciphertext = bytes.fromhex(first_block_ciphertext_hex)
recovered_plaintext_1 = strxor(first_block_ciphertext, keystream_1)

# Use the keystream_1 as new IV to generate second keystream block
keystream_hex_2 = encrypt(known_plaintext_hex, keystream_1.hex())
keystream_2 = bytes.fromhex(keystream_hex_2)

# XOR the keystream and second ciphertext block to recover second plaintext block
second_block_ciphertext = bytes.fromhex(second_block_ciphertext_hex)
recovered_plaintext_2 = strxor(second_block_ciphertext, keystream_2)

# Output both blocks as plaintext
print("Recovered first 16 bytes:", recovered_plaintext_1.decode(errors='ignore'))
print("Recovered second 16 bytes:", recovered_plaintext_2.decode(errors='ignore'))
