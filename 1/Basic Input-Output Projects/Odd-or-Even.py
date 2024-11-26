try:
    value = int(input("Enter a number: "))
    if value % 2 == 0:
        print("The number is even.")
    else:
        print("The number is odd.")
except ValueError:
        print("Invalid input. Please enter a valid integer.")