# Import the necessary libraries
from Crypto.Cipher import AES
import time
import string
import requests

# Method to call the cryptohack endpoint and encryt
def encrypt(plaintext):
    endpoint = "http://aes.cryptohack.org/ecb_oracle/encrypt/" + plaintext + "/"
    response = requests.get(endpoint)

    # Return the value from the JSON
    return response.json()['ciphertext']

# Method to loop through possible chars and compare the blocks to check if the char is correct
def check_chars(plaintext, flag_value, compare_value):

    # Create list of chars used in flags
    non_alphabet_chars = '{'+'}'+'_'+'@'

    # Loop through these chars
    for char in non_alphabet_chars:
        # Encrypt the char appended to the plaintext and current known flag value
        test_char = encrypt(bytes.hex((plaintext + flag_value + char).encode()))
        # Check if the char block matches the sample block, append it to the current flag value if it matches
        if test_char[32:64] == compare_value[32:64]:
            print("character found: " + char)
            flag_value += char
            return flag_value
        time.sleep(1)

    # Loop through lowercase letters
    for char in string.ascii_lowercase:
                # Encrypt the char appended to the plaintext and current known flag value
        test_char = encrypt(bytes.hex((plaintext + flag_value + char).encode()))
        # Check if the char block matches the sample block, append it to the current flag value if it matches
        if test_char[32:64] == compare_value[32:64]:
            print("character found: " + char)
            flag_value += char
            return flag_value
        time.sleep(1)

    # Loop through uppercase letters
    for char in string.ascii_uppercase:
        # Encrypt the char appended to the plaintext and current known flag value
        test_char = encrypt(bytes.hex((plaintext + flag_value + char).encode()))
        # Check if the char block matches the sample block, append it to the current flag value if it matches
        if test_char[32:64] == compare_value[32:64]:
            print("character found: " + char)
            flag_value += char
            return flag_value
        time.sleep(1)

    # Loop through digits (0-9)
    for char in string.digits:
        # Encrypt the char appended to the plaintext and current known flag value
        test_char = encrypt(bytes.hex((plaintext + flag_value + char).encode()))
        # Check if the char block matches the sample block, append it to the current flag value if it matches
        if test_char[32:64] == compare_value[32:64]:
            print("character found: " + char)
            flag_value += char
            return flag_value
        time.sleep(1)

# Method to crack the flag
def crack_flag():
    # Set the length at the beginning as 31
    length = 31

    # Chars will be appended as they are discovered
    flag_value = ""

    # Boolean to identify when the flag has been recovered
    flag_recovered = False

    while flag_recovered == False:
        # Create the text to compare
        plaintext = '0' * (length - len(flag_value))
        # print it
        print(plaintext)

        # Encrypt it
        compare_value = encrypt(plaintext.encode().hex())

        # Find the next char and append it to the flag
        flag_value = check_chars(plaintext, flag_value, compare_value)

        # We know the flag ends with "}" so exit when it's found
        if flag_value.endswith("}"):
            flag_recovered = True

    return flag_value

plaintext_flag = crack_flag()
print(plaintext_flag)
