import random
from shlex import split

# Таблиця усіх елементів, які можуть брати участь у грі
Element = ["rock","paper","scissors","fire","snake","tree","wolf","sponge", "human", "air", "water", "dragon",
           "devil", "lightning", "gun"]

def generate():
    return Element[random.randint(0, 2)]

def victory(man,comp: int):

    """
    Таблиця перемог для 1-ї позиції
    0-rock
    1-paper
    2-scissors
    3-fire
    4-snake
    5-tree
    6-wolf
    7-sponge
    8-human
    9-air
    10-water
    11-dragon
    12-devil
    13-lightning
    14-gun
    """

    Victory = [[0, 3], [0, 2],[0, 4],[0, 5],[0, 6],[0, 7],
               [3, 4],[3, 8],[3, 5],[3, 6],[3, 7],[3, 1],
               [2, 4],[2, 8],[2, 5],[2, 6],[2, 7],[2, 1],[2, 9],
               [4, 8],[4, 5],[4, 6],[4, 7],[4, 1],[4, 9],[4, 10],
               [8, 5],[8, 6],[8, 7],[8, 1],[8, 9],[8, 10],[8, 11],
               [5, 6],[5, 7],[5, 1],[5, 9],[5, 10],[5, 11],[5, 12],
               [6, 7],[6, 1],[6, 9],[6, 10],[6, 11],[6, 12],[6, 13],
               [7, 1],[7, 9],[7, 10],[7, 11],[7, 12],[7, 13],[7, 14],
               [1, 9],[1, 10],[1, 11],[1, 12],[1, 13],[1, 14],[1, 0],
               [9, 10],[9, 11],[9, 12],[9, 13],[9, 14],[9, 0],[9, 3],
               [10, 11],[10, 12],[10, 13],[10, 14],[10, 0],[10, 3],[10, 2],
               [11, 12],[11, 13],[11, 14],[11, 0],[11, 3],[11, 2],[11, 4],
               [12, 13],[12, 14],[12, 0],[12, 3],[12, 2],[12, 4],[12, 8],
               [13, 14],[13, 0],[13, 3],[13, 2],[13, 4],[13, 8],[13, 5],
               [14, 0],[14, 3],[14, 2],[14, 4],[14, 8],[14, 5],[14, 6]]

    if man==comp: vin="Draw"
    else:
        for i in range(Victory.__len__()):
          if Victory[i-1][1] == man and Victory[i-1][0] == comp:
              vin = "Computer"

          if Victory[i-1][0] == man and Victory[i-1][1] == comp:
              vin = "Man"


    return vin

def game_menu():
    # Таблиця номерів елементів, які беруть участь у грі
    Pole = [ ]
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
    print ("Options:")
    print("0 - rock,  1 - paper, 2 - scissors, 3 - fire,    4 - snake,  5 - tree,       6 - wolf, 7 - sponge")
    print("8 - human, 9 - air,  10 - water,   11 - dragon, 12 - devil, 13 - lightning, 14 - gun")
    options=input("Select an options:")
    if options=="": options="0 1 2"
    print("Okay, let's start.")
    select=options.split(" ")
    for i in range (len(select)): Pole.append(int(select[i]))
    man_choice=0

    while man_choice != "exit" :
       comp_choice = Pole[random.randint(0, Pole.__len__()-1)]
       for i in range(Pole.__len__()): print (Pole[i], "- ", Element[Pole[i]])
       print("rating")
       print ("exit")
       man_choice = input("Enter your choice>")
       if man_choice=="rating": print(f"Your rating: {rating}")
       if man_choice not in ["exit", "rating"]:
          try:
           if int(man_choice) in Pole:
             man_choice = int(man_choice)
             if victory(int(man_choice), comp_choice) == "Computer": print(f' Lose -> Sorry, but the computer chose {Element[comp_choice]}')
             if victory(man_choice, comp_choice) == "Man":
                 print(f' Win -> Well done. The computer chose {Element[comp_choice]}')
                 rating=rating+100
             if victory(man_choice, comp_choice) == "Draw":
                 print(f' Draw -> There is a draw {Element[comp_choice]}')
                 rating=rating+50
           else:
               print("Invalid input.")
          except ValueError:
            print("Invalid input.")


    print ("Bye!")
    return

print(game_menu())