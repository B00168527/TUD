import jwt

jwt_token = "hiding.the.token"

# Decode the JWT without verifying the signature
decoded = jwt.decode(jwt_token, options={"verify_signature": False})

print("Decoded Payload:", decoded)
