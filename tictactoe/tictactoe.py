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