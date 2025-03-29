"""
Steps:
1. Create functions to reverse step1, step2 and step3
2. Add a while loop to run while the first char is a number of 1, 2 or 3. Remove the first char if it is
3. If it's 1, run reverse of step1
4. If it's 2, run reverse of step2
5. If it's 3, run reverse of step3
6. If it's not one of those numbers, the message is decrypted so stop
"""

# Import libraries
import string
import random
from base64 import b64encode, b64decode

# Substitute letters back to their value before "step1" was applied
def step1_reverse(s):
    _step1_reverse = str.maketrans(
        "mlkjihgfedcbaMLKJIHGFEDCBAzyxwvutsrqponZYXWVUTSRQPON",
        "zyxwvutsrqponZYXWVUTSRQPONmlkjihgfedcbaMLKJIHGFEDCBA"
    )
    return s.translate(_step1_reverse)

# Decode the base64 string
def step2_reverse(s):
    return b64decode(s).decode()

# Caesar cipher shift the letters back 4 places
def step3_reverse(s, shift=-4):
    result = []
    for char in s:
        # Check if the character is lowercase, ignore the uppercase letters and numbers
        if 'a' <= char <= 'z':
            new_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
            result.append(new_char)
        else:
            # Do not shift uppercase letters and numbers
            result.append(char)
    return ''.join(result)



# Open the file in read mode
with open('intercepted.txt', 'r') as file:
    secret = file.read()

# Var to track the number of iterations. This value would be equal to the count value used in the encryption
iteration = 1

# Flag used to identify if the message is decrypted
message_is_decrypted = False

# Loop to run while message is not decrypted. This is the reverse of "make_secret"
while message_is_decrypted != True:
    # Get the first char which will determine the encryption used
    first_char = secret[0]

    # Remove the first char which is the number
    secret_without_step = secret[1:]

    # Print out the values
    print("First character of the message is: " + first_char)
    print("iteration: " + str(iteration))

    # Increment the iteration number
    iteration = iteration + 1

    # If the first char is 1, run "step1_reverse"
    if first_char == "1":
        print("Decrypting using step1_reverse")
        secret = step1_reverse(secret_without_step)
        print(secret)
    # Else if the first char is 2, run "step2_reverse"
    elif first_char == "2":
        print("Decrypting using step2_reverse")
        secret = step2_reverse(secret_without_step)
        print(secret)
    # Else if the first char is 3, run "step3_reverse"
    elif first_char == "3":
        print("Decrypting using step3_reverse")
        secret = step3_reverse(secret_without_step)
        print(secret)
    # Else the first char is not 1, 2 or 3 which means the secret is decrypted.
    else:
        # Print out the plaintext value
        print("Decrypted!!!!")
        print(secret)
        # Set the flag to true to indicate the message is decrypted and exit the loop
        message_is_decrypted = True
