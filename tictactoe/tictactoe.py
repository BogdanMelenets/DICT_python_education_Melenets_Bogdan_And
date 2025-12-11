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

def check_winner(grid):
    lines = []
    # Рядки
    for row in grid:
        lines.append(row)
    # Стовпці
    for c in range(3):
        lines.append([grid[0][c], grid[1][c], grid[2][c]])
    # Діагоналі
    lines.append([grid[0][0], grid[1][1], grid[2][2]])
    lines.append([grid[0][2], grid[1][1], grid[2][0]])
    x_win = any(line == ['X', 'X', 'X'] for line in lines)
    o_win = any(line == ['O', 'O', 'O'] for line in lines)
    # Підрахунок символів
    flat = sum(grid, [])
    x_count = flat.count("X")
    o_count = flat.count("O")
    # Перевірка "неможливого" стану
    if abs(x_count - o_count) > 1:
        return "Impossible"
    if x_win and o_win:
        return "Impossible"
    if x_win:
        return "X wins"
    if o_win:
        return "O wins"
    if "_" in flat or " " in flat:
        return "Game not finished"
    return "Draw"

