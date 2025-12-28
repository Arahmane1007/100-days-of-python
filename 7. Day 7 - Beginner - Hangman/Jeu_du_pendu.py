print("-------------------Bienvenue dans notre jeu du pendu-------------------")

liste_de_mots = [
    "chat", "maison", "livre", "pomme", "arbre", 
    "fleur", "nuit", "soleil", "ours", "pizza",
    "banane", "girafe", "avion", "manteau", "pirate",
    "salade", "tortue", "guitare", "valise", "abeille",
    "rhinoceros", "crocodile", "kangourou", "bibliotheque",
    "saxophone", "hippopotame", "pamplemousse", "grenouille",
    "escargot", "xylophone"
    ]

# Fonction pour remplacer les lettres qui va prendre en paramètre les ****** qui est une liste
# Le mot à deviner et la lettre proposée par l'utilisateur
def remplacer_lettre(mot,mot_a_deviner, lettre):
    for i in range(len(mot_a_deviner)):
        if mot_a_deviner[i] == lettre:
            mot[i] = lettre
    return mot

def afficher_pendu(chance,pendu):
    print(pendu[chance])

import random

choix_du_mot= random.choice(liste_de_mots)
taille_du_mot = len(choix_du_mot)
pendu = ["",""" 
   -----
   |   |
   O   |
       |
       |
       |""",
""" 
   -----
   |   |
   O   |
  /    |
       |
       |""",
""" 
   -----
   |   |
   O   |
  /|   |
       |
       |""",
""" 
   -----
   |   |
   O   |
  /|\  |
       |
       |""",
""" 
   -----
   |   |
   O   |
  /|\  |
  /    |
       |""",
""" 
   -----
   |   |
   O   |
  /|\  |
  / \  |
       |""",
       ]


a_deviner = "*" * taille_du_mot

print(a_deviner)

# Convertir la chaîne de caractères en liste pour pouvoir modifier les lettres
a_deviner = list(a_deviner)
chance = 0

while chance < 6  and "*" in a_deviner:
    lettre = input("Deviner une lettre : ").lower()

    if lettre in choix_du_mot:
        remplacer_lettre(a_deviner,choix_du_mot,lettre)
        print(f"Bonne réponse!✨✨\n {lettre} est dans le mot.")
    
    else:
        chance += 1
        print(f"Mauvaise réponse! 😭😭")
    
    afficher_pendu(chance,pendu)
    print("".join(a_deviner))

if chance <= 0:
    print(f"Vous avez perdu😭😭! Le mot à deviner était {choix_du_mot}.")
else:
    print("Félicitations! Vous avez gagné! 🎉🎉")