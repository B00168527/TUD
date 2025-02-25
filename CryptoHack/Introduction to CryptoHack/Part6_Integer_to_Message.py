from Crypto.Util.number import *

# The integer provided in the challenge
integer = 11515195063862318899931685488813747395775516287289682636499965282714637259206269

# Convert the long to bytes with the method provided in the steps
bytes = long_to_bytes(integer)

# print the flag
print(bytes)
