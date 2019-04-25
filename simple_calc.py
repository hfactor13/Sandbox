## This is a simple calculator program.
## Menu options that the user can input are shown below.
while True:
    print("Options: ")
    print("Enter 'add' to add two numbers.")
    print("Enter 'subtract' to subtract two numbers.")
    print("Enter 'multiply' to multiply two numbers.")
    print("Enter 'divide' to divide two numbers.")
    print("Enter 'exponentiate' to exponentiate two numbers.")
    print("Enter 'quotient' to yield the quotient of two numbers.")
    print("Enter 'remainder' to yield the remainder of two numbers.")
    print("Enter 'quit' to end the program.")
    user_input = input(": ")

    """
    At this point, the program performs the operation given
    by the user and outputs the result
    """
    
    if user_input == "quit": # Ends the program
        break
    elif user_input == "add": # Addition 
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 + num2)
        print("\n")
        print(str(num1) + ' + ' + str(num2) + ' = ' + result)
        print("\n")
    elif user_input == "subtract": # Subtraction
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 - num2)
        print("\n")
        print(str(num1) + ' - ' + str(num2) + ' = ' + result)
        print("\n")
    elif user_input == "multiply": # Multiplication
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 * num2)
        print("\n")
        print(str(num1) + ' * ' + str(num2) + ' = ' + result)
        print("\n")
    elif user_input == "divide": # Division
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 / num2)
        print("\n")
        print(str(num1) + ' / ' + str(num2) + ' = ' + result)
        print("\n")
    elif user_input == "exponentiate": # Exponentiation
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 ** num2)
        print("\n")
        print(str(num1) + ' ** ' + str(num2) + ' = ' + result)
        print("\n")
    elif user_input == "quotient": # Quotient
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 // num2)
        print("\n")
        print(str(num1) + ' // ' + str(num2) + ' = ' + result)
        print("\n")
    elif user_input == "remainder": # Remainder
        num1 = float(input("Enter a number: "))
        num2 = float(input("Enter another number: "))
        result = str(num1 % num2)
        print("\n")
        print(str(num1) + ' % ' + str(num2) + ' = ' + result)
        print("\n")
    else: #Improper input outputs this statement.
        print("\n")
        print("Unknown input. Please try again from the options listed below.")
        print("\n")
