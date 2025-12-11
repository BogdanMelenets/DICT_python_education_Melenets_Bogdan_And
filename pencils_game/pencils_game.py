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

