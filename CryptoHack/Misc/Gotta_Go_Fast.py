import json
import time
import hashlib
from pwn import remote
from Crypto.Util.number import long_to_bytes

# Send the payload to the endpoint
def get_encrypted(connection, payload):
    connection.sendline(json.dumps(payload).encode())
    # Return the response
    return connection.recvline()

# Encrypt the data like in the server code
def encrypt(data):
    timestamp = int(time.time())
    # Set the key to be the current moment
    key = hashlib.sha256(long_to_bytes(timestamp)).digest()

    # Xor the key and the already encrypted flag
    return bytes([b ^ key[i] for i, b in enumerate(data)])


def try_decrypt_flag(connection):
    # JSON to get the flag
    get_flag_payload = {"option": "get_flag"}

    # Need to loop as the server moment and my moment might be different
    while True:
        try:
            # Get the encrypted value
            response = connection.recvline()
            response = get_encrypted(connection, get_flag_payload)
            encrypted_hex = json.loads(response.decode())['encrypted_flag']
            encrypted_bytes = bytes.fromhex(encrypted_hex)

            # XOR again with same key (if timestamp matches) to retrieve original message
            decrypted_bytes = encrypt(encrypted_bytes)
            flag = decrypted_bytes.decode()

            # Print the flag and exit
            print(flag)
            break
        except Exception:
            # Likely a mismatch in timing, just try again
            continue

connection = remote('socket.cryptohack.org', 13372)
try_decrypt_flag(connection)
