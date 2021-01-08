import random

# tableau des scores
user_score = 0
cp_score = 0

# on demande le nombre de tours au joueur

user_nbr_round = int(input("Combien de manches ? "))
nbr_round = 0
while nbr_round < user_nbr_round:
    # choix du joueur
    user_choice = input("Choisis entre pierre feuille ou ciseaux : ")
    if user_choice == "pierre" or user_choice == "feuille" or user_choice == "ciseaux":

        # separation pour les manches
        print('--------------------------')

        # au tour de l'ordi
        can_use = ["pierre", "feuille", "ciseaux"]
        cp_choice = random.choice(can_use)

        # on montre le résultat de l'ordi
        print("L\'ordinateur a choisis : ", cp_choice)

        # algorithme du jeu
        if user_choice == cp_choice:
            print("Egalitée")
        elif user_choice == "pierre" and cp_choice == "feuille":
            print("L\'ordi gagne !")
            cp_score = cp_score + 1
        elif user_choice == "pierre" and cp_choice == "ciseaux":
            print("Le joueur gagne")
            user_score = user_score + 1
        elif user_choice == "feuille" and cp_choice == "pierre":
            print("Le joueur gagne")
            user_score = user_score + 1
        elif user_choice == "feuille" and cp_choice == "ciseaux":
            print("L\'ordi gagne !")
            cp_score = cp_score + 1
        elif user_choice == "ciseaux" and cp_choice == "pierre":
            print("L\'ordi gagne !")
            cp_score = cp_score + 1
        elif user_choice == "ciseaux" and cp_choice == "feuille":
            print("Le Joueur gagne !")
            user_score = user_score + 1

        nbr_round = nbr_round + 1
        print("Manche numero " + str(nbr_round) + " sur " + str(user_nbr_round))

        # on affiche le score
        print("Tu as " + str(user_score) + " points")
        print("L\'ordi a " + str(cp_score) + " points")

    else:
        print("Je ne comprends pas...")

# on determine qui a gagné
if user_score > cp_score:
    print("------Partie finie sur une victoire ! :)------")
elif cp_score > user_score:
    print("------Partie finie sur une défaite :(------")
else:
    print("------Partie finie sur une égalité :/------")
