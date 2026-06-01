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

while True:

    print("=" * 70)
    print("Stock size:", len(stock_pieces))
    print("Computer pieces:", len(computer_pieces))
    print()

    if len(domino_snake) > 6:
        print(
            ''.join(map(str, domino_snake[:3])) +
            "..." +
            ''.join(map(str, domino_snake[-3:]))
        )
    else:
        print(''.join(map(str, domino_snake)))

    print("\nYour pieces:")

    for i, piece in enumerate(player_pieces, 1):
        print(f"{i}:{piece}")

    print()

    if len(player_pieces) == 0:
        print("Status: The game is over. You won!")
        break

    if len(computer_pieces) == 0:
        print("Status: The game is over. The computer won!")
        break

    if status == "player":

        print("Status: It's your turn to make a move. Enter your command.")

        while True:
            try:
                move = int(input())
            except ValueError:
                print("Invalid input. Please try again.")
                continue

            if abs(move) > len(player_pieces):
                print("Invalid input. Please try again.")
                continue

            break

        if move == 0:
            if stock_pieces:
                player_pieces.append(stock_pieces.pop())
        elif move > 0:
            domino_snake.append(player_pieces.pop(move - 1))
        else:
            domino_snake.insert(0, player_pieces.pop(abs(move) - 1))

        status = "computer"

    else:

        print("Status: Computer is about to make a move. Press Enter to continue...")
        input()

        move = random.randint(-len(computer_pieces), len(computer_pieces))

        if move == 0:
            if stock_pieces:
                computer_pieces.append(stock_pieces.pop())

        elif move > 0:
            domino_snake.append(computer_pieces.pop(move - 1))

        else:
            domino_snake.insert(0, computer_pieces.pop(abs(move) - 1))

        status = "player"