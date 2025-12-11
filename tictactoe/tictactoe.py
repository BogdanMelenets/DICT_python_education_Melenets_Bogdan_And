def print_grid(grid):
    # Вивід поля у форматі з рамкою
    print("---------")
    for row in grid:
        print("|", " ".join(row), "|")
    print("---------")
