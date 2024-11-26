cost = float(input("What is the cost of the meal? "))
tip = float(input("What percentage would you like to tip? {eg 20% = 20}: "))

tip = tip / 100
total = cost * tip
print(f'You are to tip {total}')