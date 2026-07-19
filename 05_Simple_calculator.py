import operator     # operator is a built-in module in python containing all the efficient built-in functions that correspond to intrinsic operators.

OPERATORS = {           # Stores arithmetic operators and their functions in the dictionary in key and value pairs respectively.
    "+": operator.add,
    "-": operator.sub,
    "*": operator.mul,
    "/": operator.truediv

}


def calculate(a, symbol, b):    # A function defined for taking inputs through parameters and insert the data into the body of the function.
    if symbol in OPERATORS:     # Compares the operator input to the items listed inside the dictionary.
        return OPERATORS[symbol](a,b)   # If the operator taken through input matches any of the item listed inside the dictionary "OPERATORS", it returns the final value of the operation between the two input numbers.
           
print("Welcome to simple python calculator. In this calculator you can calculate only 2 numbers at once.")

while True:
    while True:
        try:    # Tests for whether the input is int datatype or not.
            num_1 = int(input("Enter your First number: "))
            break

        except ValueError:      # Fires when int() can't convert the input into a whole number (e.g. letters, symbols, or blank input bring out the ValueError exception.)
            print("Wrong input. Please enter the right numerical order.")
            continue

    while True:     # Not much is there to explain. Technically does all the same things as the previous block.
        try:
            num_2 = int(input("Enter your Second number: "))
            break

        except ValueError:
            print("Wrong input. Please enter the right numerical order.")
            continue


    symbol = input("Enter the operator you desire to calculate: ")
    
    
    if symbol not in OPERATORS:
        print("Error: Unknown symbol. Please try again.")
        continue
    break




print("Final answer is: ", calculate(num_1, symbol, num_2))     # The function defined in the start is called in this line.


            
