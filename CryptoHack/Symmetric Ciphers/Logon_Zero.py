from pwn import *
import json

# Set the token to be 0's
token = b'\x00' * 28
token_hex = token.hex()

# Endpoint and port for connecting
endpoint = "socket.cryptohack.org"
port = 13399

# JSON for resetting the password
reset_password_JSON = json.dumps({"option": "reset_password", "token": token_hex}).encode()
# JSON for attempting to login with empty password
authenticate_JSON = json.dumps({"option": "authenticate", "password": ""}).encode()

# Connect to the endpoint
connection = connect(endpoint, port)
connection.recvline()

# Loop until authenticate happens and the flag is found
while True:
    # Reset the password
    connection.sendline(reset_password_JSON)
    reset_password_response = connection.recvline()
    print(reset_password_response.decode())

    # Attempt to login
    connection.sendline(authenticate_JSON)
    authenticate_response = connection.recvline()
    print(authenticate_response.decode())

    # Check if the login was successful flag was found
    if "crypto{" in authenticate_response.decode():
        print("Found the flag")
        # Break out of the loop
        break

    # Reset the connection if the flag was not found
    connection.sendline(json.dumps({"option": "reset_connection"}))
    reset_connection_response = connection.recvline()
    print(reset_connection_response.decode())
