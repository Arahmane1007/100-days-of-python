print("Welcome to python pizza delivery!")

size = input("What size pizza do you want? S, M, or L ")
add_peperroni = input("Do you want pepperoni? Y or N ")
extra_cheese = input("Do you want extra cheese? Y or N ")

size_price = 15 if size == 'S' else 20 if size == 'M' else 25 if size == 'L' else 0

add_pepperoni_price = 2 if add_peperroni == 'Y' and size == 'S' else 3 if add_peperroni == 'Y' else 0

extra_cheese_price = 1 if extra_cheese == 'Y' else 0

print(f"Your final bill is: ${size_price + add_pepperoni_price + extra_cheese_price}")