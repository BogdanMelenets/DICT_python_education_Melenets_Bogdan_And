def print_static_grid():
    print("X O X")
    print("O X O")
    print("X X O")

def print_grid(cells):
    # Друк рамки
    print("---------")
    # Виводимо 3 рядки по 3 символи
    for i in range(0, 9, 3):
        print("|", cells[i], cells[i+1], cells[i+2], "|")
    print("---------")

def check_win(cells):
    wins = [
        (0, 1, 2), (3, 4, 5), (6, 7, 8),      # рядки
        (0, 3, 6), (1, 4, 7), (2, 5, 8),      # колонки
        (0, 4, 8), (2, 4, 6)                  # діагоналі
    ]

    x_win = False
    o_win = False

    for a, b, c in wins:
        line = cells[a] + cells[b] + cells[c]
        if line == "XXX":
            x_win = True
        if line == "OOO":
            o_win = True

    count_x = cells.count("X")
    count_o = cells.count("O")

    # Неможливі стани
    if abs(count_x - count_o) > 1:
        return "Impossible"
    if x_win and o_win:
        return "Impossible"

    if x_win:
        return "X wins"
    if o_win:
        return "O wins"

    if "_" in cells:
        return "Game not finished"
    return "Draw"

def user_move(cells):
    while True:
        coords = input("Enter the coordinates: ").split()

        # Перевірка на числа
        if not all(c.isdigit() for c in coords):
            print("You should enter numbers!")
            continue

        x, y = map(int, coords)

        # Перевірка діапазону
        if x not in [1, 2, 3] or y not in [1, 2, 3]:
            print("Coordinates should be from 1 to 3!")
            continue

        # Перетворення координат в індекс
        index = (x - 1) * 3 + (y - 1)

        # Перевірка зайнятості
        if cells[index] != "_":
            print("This cell is occupied! Choose another one!")
            continue

        # Робимо хід
        cells[index] = "X"
        return cells