
print("Welcome to our leap year checker!!!")

year = int(input("Which year do you want to check?\n"))

is_leap_year = True if year%4==0 and (year%100 !=0 or year%400==0) else False

if is_leap_year:
    print(f"{year} is a leap year.")
else:
    print(f"{year} is not a leap year.")

