"""CLI application for a prefix-notation calculator."""

from arithmetic import (add, subtract, multiply, divide, square, cube,
                        power, mod, )


# if the token is "add" 
#   then call the add function with the remaining two tokens

# repeat forever:

while True:
#     read input
    equation = input("Enter your equation here: ")  
#     tokenize input
    tokens = equation.split(' ')
    
#         if the first token is "q":
    first = tokens[0]
    print(first)
    if first =='q':
        break
    print(tokens)

#             quit
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens