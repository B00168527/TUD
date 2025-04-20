import requests

# Endpoint for calls
endpoint = "http://aes.cryptohack.org/lazy_cbc/"

# Encrypt 16 0's
encrypt_url = endpoint + "encrypt/00000000000000000000000000000000"
encrypt_response = requests.get(encrypt_url)
# Get the resulting ciphertext
ciphertext = encrypt_response.json().get("ciphertext")

# Call the receive request with null block first appended with the ciphertext
received_url = endpoint + "receive/00000000000000000000000000000000" + ciphertext
decrypted = requests.get(received_url)

# Filter out the message
decrypted_response = decrypted.json().get("error").split(": ")[1]
# Get the second block
second_block = decrypted_response[-32:]

# Pass the second block which is the key
get_flag_url = endpoint + "get_flag/" + second_block
flag_response = requests.get(get_flag_url)
flag_hexed = flag_response.json().get("plaintext")

# Convert the flag from hex to plaintext and print it
flag = bytes.fromhex(flag_hexed).decode('ascii')
print(flag)
