def bytes2matrix(text):
    """ Converts a 16-byte array into a 4x4 matrix.  """
    return [list(text[i:i+4]) for i in range(0, len(text), 4)]

def matrix2bytes(matrix):
    """ Converts a 4x4 matrix into a 16-byte array.  """
    # Convert the matrix to an array
    byte_array = [byte for row in matrix for byte in row]
    flag = ""
    # Loop through the array and convert each byte to a char and append it to the flag value
    for byte in byte_array:
        flag = flag + chr(byte)

    # Return the flag    
    return flag

matrix = [
    [99, 114, 121, 112],
    [116, 111, 123, 105],
    [110, 109, 97, 116],
    [114, 105, 120, 125],
]

print(matrix2bytes(matrix))
