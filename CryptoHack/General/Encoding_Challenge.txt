To solve this challenge, I create a function named "solve_level" which reversed the encoding done in the python file provided.
The function checks the JSON value provided to retrieve the "type" of encoding that was done. 
The code then simply uses this type to check if else statements to find the correct decoding line to call. 
This decoded value is returned.
The main part of code calls a for loop which runs 100 times. Inside the loop, the JSON is retrieved from the endpoint and passed into the "solve_level" function. 
The value returned from "solve_level" is checked to see if it contains the word "flag". If it does, the loop breaks.
If it doesn't, the value is send back to the endpoint and the next value is retrieved. 
