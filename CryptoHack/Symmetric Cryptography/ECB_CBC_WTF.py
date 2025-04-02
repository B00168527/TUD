from Crypto.Cipher import AES
import requests
from pwn import xor

# Method to call the cryptohack endpoint and encryt
def encrypt():
    endpoint = "http://aes.cryptohack.org/ecbcbcwtf/encrypt_flag/"
    response = requests.get(endpoint)

    # Return the value from the JSON
    return response.json()['ciphertext']

# Method to call the cryptohack endpoint and decrypt
def decrypt(block):
    endpoint = "http://aes.cryptohack.org/ecbcbcwtf/decrypt/" + str(block) + '/'
    response = requests.get(endpoint)

    # Return the value from the JSON
    return response.json()['plaintext']

# Get the ciphertext
ciphertext = encrypt()

# Block sizes
blocks = [0, 32, 64]
ciphered_blocks = []

# Split up the ciphertext into the blocks
for block in blocks:
    ciphered_blocks.append(ciphertext[block:block+32])

# All blocks except the last
init_vector = ciphered_blocks[0:(len(ciphered_blocks) - 1)]

# Remove the first vloack
ciphered_blocks = ciphered_blocks[1:]

# Print for debugging
print(init_vector)
print(ciphered_blocks)

# Decrypt each block using ECB
for block_index in range(len(ciphered_blocks)):
    ciphered_blocks[block_index] = decrypt(ciphered_blocks[block_index])

# Use XOR to reverse the CBC
for i in range(len(ciphered_blocks)):
    ciphered_blocks[i] = xor(bytes.fromhex(ciphered_blocks[i]), bytes.fromhex(init_vector[i]))

# Reconstruct the flag by adding the decoded blocks
plaintext = ""
for block in ciphered_blocks:
    decoded_block = block.decode()
    plaintext += decoded_block

print(plaintext)
