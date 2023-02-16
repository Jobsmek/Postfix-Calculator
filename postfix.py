# from module import method
from stack import Stack
from operations import operations
from numberChecker import numberChecker
import math

#Create a stack
stack = Stack()

# Prompts and records user's input
userInput = input("Enter Function with spaces between digits and operands:")

# Splits the input into a list by the spaces
# So    1 3 +  becomes ['1', '3', '+']
splitInput = userInput.split( )  

i = 0   # initializes incrimentor
while i < len(splitInput):
    if numberChecker.check(splitInput[i]) == True: # If i is a number not math.isnan(splitInput[i])   splitInput[i].isdigit
        stack.push(splitInput[i])
        
    elif splitInput[i] == "+":
        # print("This will call the operations add class")
        num1 = stack.pop()
        # print(num1)
        num2 = stack.pop()
        # print(num2)
        num3 = operations.add(num1, num2)
        # print(num3, "This is the result")
        stack.push(num3)
        
    elif splitInput[i] == "-":
        try:
            num1 = stack.pop()
            num2 = stack.pop()
            num3 = operations.sub(num1, num2)
            stack.push(num3)
        except:
            print("Error")

    elif splitInput[i] == "/":
        try:
            num1 = stack.pop()
            num2 = stack.pop()
            num3 = operations.div(num1, num2)
            stack.push(num3)
        except:
            print("Error")

    elif splitInput[i] == "*":
        try:
            num1 = stack.pop()
            num2 = stack.pop()
            num3 = operations.mult(num1, num2)
            stack.push(num3)
        except:
            print("Error")

    elif splitInput[i] == "^":
        try:
            num1 = stack.pop()
            num2 = stack.pop()
            num3 = operations.pow(num1, num2)
            stack.push(num3)
        except:
            print("Error")
    
    else:
        print("Error")
        break
    i = i + 1   #IMPORTANT incriments loop

# Print out the result 
lastNumber = stack.pop()
print(lastNumber)