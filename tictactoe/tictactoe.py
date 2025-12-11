def print_grid(grid):
    # Вивід поля у форматі з рамкою
    print("---------")
    for row in grid:
        print("|", " ".join(row), "|")
    print("---------")

def string_to_grid(cells):
    grid = [
        [cells[0], cells[1], cells[2]],
        [cells[3], cells[4], cells[5]],
        [cells[6], cells[7], cells[8]]
    ]
    return grid
