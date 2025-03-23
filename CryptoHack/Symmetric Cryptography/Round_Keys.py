state = [
    [206, 243, 61, 34],
    [171, 11, 93, 31],
    [16, 200, 91, 108],
    [150, 3, 194, 51],
]

round_key = [
    [173, 129, 68, 82],
    [223, 100, 38, 109],
    [32, 189, 53, 8],
    [253, 48, 187, 78],
]

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

def add_round_key(s, k):
    # Create a temp matrix to store the result
    temp_matrix = [
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
        [0, 0, 0, 0],
    ]

    # Loop through each row and column
    for row in range(4):
        for col in range(4):
            # XOR each cell of s and k. Store the result in the corresponding cell of the temp matrix
            temp_matrix[row][col] = s[row][col]^k[row][col]
    return(matrix2bytes(temp_matrix))


print(add_round_key(state, round_key))
