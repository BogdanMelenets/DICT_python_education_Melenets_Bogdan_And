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