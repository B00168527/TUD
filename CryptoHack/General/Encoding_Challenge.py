from pwn import *
import json
import base64
import codecs


# Function to decode based on the encoded type. Reverses the encoding done in the python file provded
def solve_level(encoded_obj):
    encoding = encoded_obj["type"]
    encoded = encoded_obj["encoded"]

    # Decode the base64
    if encoding == "base64":
        decoded = base64.b64decode(encoded).decode('utf-8')
    # Decode the hex
    elif encoding == "hex":
        decoded = binascii.unhexlify(encoded).decode('utf-8')
    # Decode the rot13
    elif encoding == "rot13":
        decoded = codecs.encode(encoded, 'rot_13')
    # Decode the bigint
    elif encoding == "bigint":
        # Remove '0x' if present and convert back to bytes
        decoded = binascii.unhexlify(encoded.replace('0x', '')).decode('utf-8')
    # Decode the utf-8
    elif encoding == "utf-8":
        decoded = ""
        for c in encoded:
            decoded += chr(c)
    # Return the decoded value
    return decoded

# Provided
r = remote('socket.cryptohack.org', 13377, level = 'debug')
# Function provided
def json_recv():
    line = r.recvline()
    return json.loads(line.decode())

# Function provided
def json_send(hsh):
    request = json.dumps(hsh).encode()
    r.sendline(request)



# Loop until the flag is found
for i in range(101):
    print(i)
    # Use the function provided to retrieve the encoded value
    received = json_recv()

    # Check if the returned value contains the word "flag"
    if "flag" in received:
        # Print the flag and break out of the loop
        print(received)
        break

    # Flag is not found, decrypt again
    received = solve_level(received)

    # Create JSON to send
    to_send = {
        "decoded": received
    }

    # Send the level
    json_send(to_send)
