# ASCII provided in the challenge
ascii = [99, 114, 121, 112, 116, 111, 123, 65, 83, 67, 73, 73, 95, 112, 114, 49, 110, 116, 52, 98, 108, 51, 125]

# Set the flag to empty
flag = ""

# Loop through each ASCII and append it to the flag
for i in ascii:
    flag = flag + chr(i)
    print(chr(i))

# Print the flag
print(flag)
