import random


rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

choice = [rock, paper, scissors]

your_choice = choice[int(input("Quel est votre choix? 0 pour pierre, 1 pour papier, 2 pour ciseaux\n"))]
computer_choice = choice[random.randint(0, 2)]

print(f"Vous avez choisi:\n{your_choice}")
print(f"L'ordinateur a choisi:\n{computer_choice}")

if (your_choice == computer_choice):
    print("Égalité!")
elif (your_choice == rock and computer_choice ==scissors) or (your_choice == paper and computer_choice == rock) or (your_choice == scissors and computer_choice==paper):
    print("Vous gagnez!")
else:
    print("Vous perdez!")