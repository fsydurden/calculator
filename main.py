from art import logo
print(logo)
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

addition = add

operations = {"+": add ,
             "-": sub ,
             "*": mul ,
             "/": div ,}

# print(operations["*"](4,8))

num1 = int(input("Enter the first number: \t"))
choice = str(input("What operation do you want to perform "
                   "+ for addition\n"
                   "- for substraction\n"
                   "* for multiplication\n"
                   "/ for division\n"
                   "enter your choice \t"))
num2 = int(input("Enter second number: \t"))

def calculation(number1, number2, choices):
    result = 0
    if choices == "+":
        result = operations["+"](number1, number2)
    elif choices == "-":
        result = operations["-"](number1, number2)
    elif choices == "*":
        result = operations["*"](number1, number2)
    elif choices == "/":
        result = operations["/"](number1, number2)
    else:
        print("Invalid choice")
    # print(result)
    return result

working = True
while working:
    pre_result = calculation(num1, num2,choice)
    print(pre_result)
    need = str(input("Press y if you want to continue with previous result or enter n for new calculation"))
    if need == "y":
        num1 = pre_result
        choice = str(input("What operation do you want to perform "
                           "+ for addition\n"
                           "- for substraction\n"
                           "* for multiplication\n"
                           "/ for division\n"
                           "enter your choice \t"))
        num2 = int(input("Enter second number: \t"))

        calculation(pre_result, num2,choice)
    elif need == "n":
        print("\n" * 100)
        num1 = int(input("Enter the first number: \t"))
        choice = str(input("What operation do you want to perform "
                           "+ for addition\n"
                           "- for substraction\n"
                           "* for multiplication\n"
                           "/ for division\n"
                           "enter your choice \t"))
        num2 = int(input("Enter second number: \t"))
        pre_result = calculation(num1, num2, choice)

    else:
        print("Invalid input. Exiting calculator.")
        working = False
