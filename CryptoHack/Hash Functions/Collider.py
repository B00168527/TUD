from pwn import remote

# The two strings of bytes causing the collision were found on https://crypto.stackexchange.com/questions/1434/are-there-two-known-strings-which-have-the-same-md5-hash-value
connection = remote('socket.cryptohack.org', 13389, level='DEBUG')
connection.recv()

# Send the first hash collision value
connection.sendline(b'{\"document\": \"d131dd02c5e6eec4693d9a0698aff95c2fcab50712467eab4004583eb8fb7f8955ad340609f4b30283e4888325f1415a085125e8f7cdc99fd91dbd7280373c5bd8823e3156348f5bae6dacd436c919c6dd53e23487da03fd02396306d248cda0e99f33420f577ee8ce54b67080280d1ec69821bcb6a8839396f965ab6ff72a70\"}')
connection.recv()

# Send the second hash collision value
connection.sendline(b'{\"document\": \"d131dd02c5e6eec4693d9a0698aff95c2fcab58712467eab4004583eb8fb7f8955ad340609f4b30283e488832571415a085125e8f7cdc99fd91dbdf280373c5bd8823e3156348f5bae6dacd436c919c6dd53e2b487da03fd02396306d248cda0e99f33420f577ee8ce54b67080a80d1ec69821bcb6a8839396f9652b6ff72a70\"}')
# Collect the flag and print it out
flag = connection.recv()
print(flag)
