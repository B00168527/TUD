from Crypto.Util.number import *
from pwn import *

# The message provided in the challenge
message = "0e0b213f26041e480b26217f27342e175d0e070a3c5b103e2526217f27342e175d0e077e263451150104"

# The template that the flags all follow
flag_template = "crypto{"
# Override the value when I have the key obtained from first XOR'ing with the value above
flag_template = "myXORkey"

# Convert the flag template to hex
flag_hex_value = flag_template.encode().hex()
print(flag_hex_value)

# Convert both hex to bytes
message_to_bytes = bytes.fromhex(message)
flag_to_bytes = bytes.fromhex(flag_hex_value)

# XOR the two values
result = xor(message_to_bytes, flag_to_bytes)
# print the flag
print(result)
