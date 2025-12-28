import random 
print("Welcome to our Py Password generator")

number_of_letter = int(input("How many letter would you like to be on your password?"))

number_of_symbols = int(input("How many symbols would you like?"))

number_of_numbers = int(input("How many numbers would you like?"))

letters = [ 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
            'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',
            'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M',
            'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']

final_password = []

for letter in range(0, number_of_letter):
    final_password.append(letters[random.randint(0,len(letters)-1)])

for symbol in range(0, number_of_symbols):
    final_password.append(symbols[random.randint(0,len(symbols)-1)])

for number in range(0, number_of_numbers):
    final_password.append(numbers[random.randint(0,len(numbers)-1)])

random.shuffle(final_password)

print("Your password is: " + "".join(final_password))

