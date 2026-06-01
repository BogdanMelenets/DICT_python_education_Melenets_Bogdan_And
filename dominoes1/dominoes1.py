import random

while True:
    domino_set = []

    for i in range(7):
        for j in range(i, 7):
            domino_set.append([i, j])

    random.shuffle(domino_set)

    player_pieces = domino_set[:7]
    computer_pieces = domino_set[7:14]
    stock_pieces = domino_set[14:]

    player_doubles = [x for x in player_pieces if x[0] == x[1]]
    computer_doubles = [x for x in computer_pieces if x[0] == x[1]]

    if not player_doubles and not computer_doubles:
        continue

    max_player = max(player_doubles) if player_doubles else [-1, -1]
    max_computer = max(computer_doubles) if computer_doubles else [-1, -1]

    if max_player > max_computer:
        domino_snake = [max_player]
        player_pieces.remove(max_player)
        status = "computer"
    else:
        domino_snake = [max_computer]
        computer_pieces.remove(max_computer)
        status = "player"

    break

print("Stock pieces:", stock_pieces)
print("Computer pieces:", computer_pieces)
print("Player pieces:", player_pieces)
print("Domino snake:", domino_snake)
print("Status:", status)

print("=" * 70)

print("Stock size:", len(stock_pieces))
print("Computer pieces:", len(computer_pieces))

print()
print(*domino_snake, sep="")

print()
print("Your pieces:")

for i, piece in enumerate(player_pieces, 1):
    print(f"{i}:{piece}")

print()

if status == "player":
    print("Status: It's your turn to make a move. Enter your command.")
else:
    print("Status: Computer is about to make a move. Press Enter to continue...")