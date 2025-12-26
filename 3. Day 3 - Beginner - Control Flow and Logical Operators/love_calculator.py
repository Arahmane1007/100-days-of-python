print("Welcome to our python love calculator")

name1= input("What's your name? \n")

name2= input("What's their name? \n")

combined_names = name1.lower() + name2.lower()
final_true = 0
final_love = 0
for letter in combined_names:
    count_t = int(letter == 't')
    count_r = int(letter == 'r')
    count_u = int(letter == 'u')
    count_e = int(letter == 'e')
    count_l = int(letter == 'l')
    count_o = int(letter == 'o')
    count_v = int(letter == 'v')
    final_true += (count_t + count_r + count_u + count_e)
    final_love += (count_l + count_o + count_v + count_e)

love_score = int(str(final_true) + str(final_love))

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")