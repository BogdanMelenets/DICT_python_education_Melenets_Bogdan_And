import random
# Таблиця усіх елементів, які можуть брати участь у грі
Element = ["rock","paper","scissors"]

def generate():
    return Element[random.randint(0, 2)]

def victory(man: int):
    # Таблиця перемог для 1 гравця
    Victory = [[0, 2], [2, 1], [1, 0]]
    vin=1000
    for i in range(3):
        if Victory[i-1][1] == man: vin=Victory[i-1][0]
    return vin

def game_menu():
    # Таблиця номерів елементів, які беруть участь у грі
    Pole = [0, 1, 2]
    man_choice=" "
    for i in range(Pole.__len__()): print (i, "- ", Element[i])
    man_choice = int(input("Enter your choice>"))
    print (f'Sorry, but the computer chose {Element[victory(man_choice)]}')
    return

print(game_menu())