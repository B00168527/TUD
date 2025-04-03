import requests
from datetime import datetime, timedelta
import binascii

# Method to get the encrypted cookie
def get_encrypted_cookie():
    response = requests.get("http://aes.cryptohack.org/flipping_cookie/get_cookie/").json()
    return response["cookie"]

# Method to perform bit flipping on the cookie, changes False to True
def modify_cookie(cookie, plaintext):

    # Convert hex-encoded cookie to bytes
    cookie_bytes = bytes.fromhex(cookie)

    # Locate "admin=False" in the expected plaintext
    target_index = plaintext.find(b"admin=False")

    # Set the replacement string ";admin=True;"
    replacement = b";admin=True;"

    # Initialize a modified IV
    modified_iv = bytearray([0xff] * 16)

    # Convert cookie to mutable bytearray
    modified_cookie = bytearray(cookie_bytes)

    # Apply bit-flipping to modify the decrypted text
    for i in range(len(replacement)):
        modified_cookie[16 + i] = plaintext[16 + i] ^ cookie_bytes[16 + i] ^ replacement[i]
        modified_iv[target_index + i] = plaintext[target_index + i] ^ cookie_bytes[target_index + i] ^ replacement[i]

    # Convert modified IV and cookie back to hex
    return modified_cookie.hex(), modified_iv.hex()

def check_admin(cookie, iv):
    # Sends the modified cookie to the endpoint
    check_admin_endpoint = f"http://aes.cryptohack.org/flipping_cookie/check_admin/{{}}/{{}}/"

    # Get the response from the endpoint
    response = requests.get(check_admin_endpoint.format(cookie, iv)).json()
    return response

# Generate the plaintext format used in encryption
expires_at = (datetime.today() + timedelta(days=1)).strftime("%s")
plaintext = f"admin=False;expiry={expires_at}".encode()

# Get an encrypted cookie from the server
cookie = get_encrypted_cookie()

# Perform the attack by modifying the cookie
modified_cookie, modified_iv = modify_cookie(cookie, plaintext)

# Send the modified cookie to the endpoint
result = check_admin(modified_cookie, modified_iv)

# Print the response
print(result)
