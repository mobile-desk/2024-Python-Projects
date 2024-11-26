import datetime

print("Welcome to the age calculator")
year=int(input("Enter your birth year:"))
print(f"Months are representes as follows \n January=1 \n February=2 \n March=3 \n April=4 \n May=5 \n June=6 \n July=7 \n August=8 \n September=9 \n October=10 \n November=11 \n December=12")
try:
    month=int(input("Enter your birth month:"))
except:
    print("Invalid input")



def get_current_month():
    # Get the current date
    current_date = datetime.datetime.now()
    # Extract the current month
    current_month = current_date.month
    return current_month


def get_current_year():
    # Get the current date
    current_date = datetime.datetime.now()
    # Extract the current year
    current_year = current_date.year
    return current_year



def get_current_day_of_month():
    # Get the current date
    current_date = datetime.datetime.now()
    # Extract the current day of the month
    current_day = current_date.day
    return current_day


if month > get_current_month():
    current_year = get_current_year() - 1
    print(f"Your age is {current_year - year} years old")

elif month < get_current_month():
    current_year = get_current_year()
    print(f"Your age is {current_year - year} years old")

else:
    day = input("Enter your birth day: ")
    if day < get_current_day_of_month():
        current_year = get_current_year() - 1
        print(f"Your age is {current_year - year} years old")

    else:
        current_year = get_current_year()
        print(f"Your age is {current_year - year} years old")









