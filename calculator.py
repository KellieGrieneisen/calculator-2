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
    calc = tokens[0]
    num1 = int(tokens[1])
    num2 = int(tokens[2])
    if calc =='q':
        break
    #print(tokens)
    elif calc == '+' or calc == 'add':
        #call add function on token[1] and token[2]
        addition = add(float(num1), float(num2))
        print(addition)
        #print output of add function



    
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens