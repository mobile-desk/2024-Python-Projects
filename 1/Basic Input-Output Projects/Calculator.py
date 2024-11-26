def action(op):
    op = op.strip()
    if op == '1':
        value = input("Enter all numbers you wish to add, seperated by a comma: ")
        values = value.split(",")
        for i in range(len(values)):
            values[i] = int(values[i])
        return add(*values)
    
    elif op == '2':
        main_value = input("Enter the number you wish to subtract from: ")
        main_value = int(main_value)
        value = input("Enter all numbers you wish to subtract, seperated by a comma: ")
        values = value.split(",")
        for i in range(len(values)):
            values[i] = -int(values[i])
        return sub(main_value, *values)
    
    elif op == '3':
        value = input("Enter all numbers you wish to multiply, seperated by a comma: ")
        values = value.split(",")
        for i in range(len(values)):
            values[i] = int(values[i])
        return mult(*values)
    
    elif op == '4':
        num = input("Enter the numerator: ")
        den = input("Enter the denominator: ")
        return div(int(num), int(den))

    elif op == '5':
        base = input("Enter the base: ")
        exp = input("Enter the exponent: ")
        return expon(int(base), int(exp))

    else:
        return 'invalid input'
    



def add(*values):
    try:
        total = 0
        for value in values:
            total += value
        return total
    except:
        return "Invalid input"



def sub(main_value, *values):
    try:
        total = main_value
        for value in values:
            total += value
        return total
    except:
        return "Invalid input"



def mult(*values):
    try:
        total = 1
        for value in values:
            total *= value
        return total
    except:
        return "Invalid input"


def div(num, den):
    try:
        return num / den
    except:
        return "Invalid input"


def expon(base, exp):
    try:
        return base ** exp
    except:
        return "Invalid input"


print("Welcome to the calculator!")
print("What would you like to do?")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")
print("5. Exponentiation")


op = input("Enter your choice: ")
print(action(op))