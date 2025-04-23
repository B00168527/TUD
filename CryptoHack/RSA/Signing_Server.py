import json
from pwn import *

# Connect to the endpoint
connection = remote('socket.cryptohack.org', 13374)
connection.recvline()

# Get the secret value
connection.sendline(json.dumps({'option': 'get_secret'}).encode())
secret = json.loads(connection.recvline().decode())['secret']

# Send the secret to get it signed
connection.sendline(json.dumps({'option': 'sign', 'msg': secret}).encode())
signature = json.loads(connection.recvline().decode())['signature']

# Print out the flag/secret
print(signature)
