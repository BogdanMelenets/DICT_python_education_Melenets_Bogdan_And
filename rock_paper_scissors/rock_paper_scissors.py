import random
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
    man_choice=0
    comp_choice=random.randint(0, 2)
    for i in range(Pole.__len__()): print (i, "- ", Element[i])
    man_choice = int(input("Enter your choice>"))
    if victory(man_choice,comp_choice)=="Computer": print(f' Sorry, your lost, but the computer chose {Element[comp_choice]}')
    if victory(man_choice, comp_choice) == "Man": print(f' You won! The computer chose {Element[comp_choice]}')
    if victory(man_choice, comp_choice) == "Draw": print(f' There is a draw, but the computer chose {Element[comp_choice]}')
    return

print(game_menu())