import jwt

username = 'brian'
admin_flag = 'true'
algo = 'HS256'
# Taken from the readme docs
SECRET_KEY = "secret"

encoded = jwt.encode({'username':username,'admin':admin_flag},SECRET_KEY,algorithm=algo)

print(encoded)
