import random
from shlex import split

# Таблиця усіх елементів, які можуть брати участь у грі
Element = ["rock","paper","scissors"]

def generate():
    return Element[random.randint(0, 2)]

def victory(man,comp: int):
    # Таблиця перемог для 1 гравця
    Victory = [[0, 2], [2, 1], [1, 0]]
    if man==comp: vin="Draw"
    else:
        for i in range(3):
          if Victory[i-1][1] == man and Victory[i-1][0] == comp: vin = "Computer"
          if Victory[i-1][1] == man and Victory[i-1][0] != comp: vin = "Man"

    return vin

def game_menu():
    # Таблиця номерів елементів, які беруть участь у грі
    Pole = [0, 1, 2]
    man_name=input("Enter your name: >")
    print (f'Hello, {man_name}')
    with open('rating.txt', 'r', encoding='utf-8') as f:
        lines = f.readlines()
        f.close()
    rating=0
    for item in lines:
        if item.find("/")>-1:
            name_rating=item.replace("\n","").split("/")
            if name_rating[0]==man_name: rating=int(name_rating[1])

    man_choice=0
    comp_choice=random.randint(0, 2)
    while man_choice != "exit" :
       for i in range(Pole.__len__()): print (i, "- ", Element[i])
       print("rating")
       print ("exit")
       man_choice = input("Enter your choice>")
       if man_choice=="rating": print(f"Your rating: {rating}")
       if man_choice not in ["exit", "rating"]:
          try:
           if int(man_choice) in Pole:
             man_choice = int(man_choice)
             if victory(int(man_choice), comp_choice) == "Computer": print(f' Sorry, your lost, but the computer chose {Element[comp_choice]}')
             if victory(man_choice, comp_choice) == "Man":
                 print(f' You won! The computer chose {Element[comp_choice]}')
                 rating=rating+100
             if victory(man_choice, comp_choice) == "Draw":
                 print(f' There is a draw, but the computer chose {Element[comp_choice]}')
                 rating=rating+50
           else:
               print("Invalid input.")
          except ValueError:
            print("Invalid input.")


    print ("Bye!")
    return

print(game_menu())