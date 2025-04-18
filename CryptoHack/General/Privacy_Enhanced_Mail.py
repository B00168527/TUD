from Crypto.PublicKey import RSA
# Open the file
with open("privacy_enhanced_mail.pem", "rb") as f:
        # Read the key
        key = RSA.import_key(f.read())
        # Print the key in decimal form
        print(f"Private exponent d: {key.d}")
