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
    
    if len(tokens) < 3:
        num2 ='0'
    else:
        num2 = int(tokens[2]) 

    if 'q' in tokens:
        break
    #print(tokens)
    elif calc == '+' or calc == 'add':
        #call add function on token[1] and token[2]
        addition = add(float(num1), float(num2))
        print(addition)
        #print output of add function
    elif calc == '-' or calc == 'subtract':
        #call subtraction function on token[1] and token[2]
        subtraction = subtract(float(num1), float(num2))
        print(subtraction)
    elif calc == '*' or calc == 'multiply':
        #call multiplication function on token[1] and token[2]
        multiplication = multiply(float(num1), float(num2))
        print(multiplication)
    elif calc == '/' or calc == 'divide':
        #call division function on token[1] and token[2]
        division = divide(float(num1), float(num2))
        print(division)
    elif calc == 'square':
        #call square function on token[1] and token[2]
        squared = square(float(num1))
        print(squared)
    elif calc == 'cube':
        #call cube function on token[1] and token[2]
        cubed = cube(float(num1))
        print(cubed)
    elif calc == 'power':
        #call power function on token[1] and token[2]
        powered = power(float(num1), float(num2))
        print(powered)
    elif calc == 'mod':
        #call mod function on token[1] and token[2]
        mode = mod(float(num1), float(num2))
        print(mode)


    
#         else:
#             (decide which math function to call based on first token)
#             if the first token is 'pow':
#                   call the power function with the other two tokens