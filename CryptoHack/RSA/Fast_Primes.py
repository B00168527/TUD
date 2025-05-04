from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_OAEP
from Crypto.Util.number import long_to_bytes


def extended_gcd(a, b):
    if a == 0:
        return b, 0, 1
    gcd, x, y = extended_gcd(b % a, a)
    return gcd, y - (b // a) * x, x


def load_rsa_key(filepath):
    with open(filepath, 'rb') as key_file:
        return RSA.importKey(key_file.read())


def rsa_decrypt(ciphertext, n, e, p, q):
    """Decrypt the ciphertext using RSA private key components."""
    # Compute the RSA private key
    phi = (p - 1) * (q - 1)
    _, a, b = extended_gcd(phi, e)
    d = b % phi

    # Construct RSA key
    key = RSA.construct((n, e, d, p, q))
    cipher = PKCS1_OAEP.new(key)
    return cipher.decrypt(ciphertext)


# Load the RSA key
key = load_rsa_key("key.pem")

# Extract RSA key components
n = key.n
e = key.e

# Ciphertext to decrypt
ciphertext = bytes.fromhex("249d72cd1d287b1a15a3881f2bff5788bc4bf62c789f2df44d88aae805b54c9a94b8944c0ba798f70062b66160fee312b98879f1dd5d17b33095feb3c5830d28")

# Known prime factors (in the case of a weak RSA key vulnerable to ROCA)
p = 51894141255108267693828471848483688186015845988173648228318286999011443419469
q = 77342270837753916396402614215980760127245056504361515489809293852222206596161

# Decrypt the message
decrypted_message = rsa_decrypt(ciphertext, n, e, p, q)
print(decrypted_message)
