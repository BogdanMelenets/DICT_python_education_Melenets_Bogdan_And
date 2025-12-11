import random
while True:
    pencils = input("How many pencils would you like to use:\n")
    if not pencils.isdigit():                       # Перевірка: чи це число
        print("The number of pencils should be numeric")
        continue
    pencils = int(pencils)
    if pencils <= 0:                                # Перевірка: число додатне
        print("The number of pencils should be positive")
        continue
    break

# Імена гравців
user = "John"
bot = "Jack"

while True:
    first = input(f"Who will be the first ({user}, {bot}):\n")
    if first not in [user, bot]:
        print(f"Choose between '{user}' and '{bot}'")
        continue
    break
# Виводимо стартову кількість олівців
print("|" * pencils)
current_player = first   # Хто ходить зараз

def bot_move(pencils_left):
    # Програшні позиції: 1, 5, 9, 13...
    if pencils_left % 4 == 1:
        return random.randint(1, 3)  # Беремо будь-яке число
    # Виграшні позиції:
    if pencils_left % 4 == 0:
        return 3
    if pencils_left % 4 == 3:
        return 2
    if pencils_left % 4 == 2:
        return 1

while pencils > 0:
    print(f"{current_player}'s turn:")
    # Хід користувача
    if current_player == user:
        move = input()
        if move not in ["1", "2", "3"]:    # Перевірка правильності
            print("Possible values: '1', '2' or '3'")
            continue
        move = int(move)
        if move > pencils:  # Забагато взято
            print("Too many pencils were taken")
            continue
    # Хід бота
    else:
        move = bot_move(pencils)   # Хід бота за стратегією
        print(move)
    # Зменшуємо кількість олівців
    pencils -= move
    if pencils == 0:
        break
    print("|" * pencils)
    # Зміна гравця
    current_player = bot if current_player == user else user
# Визначення переможця
winner = bot if current_player == user else user
print(f"{winner} won!")