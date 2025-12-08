import random
num_friends = int(input("Enter the number of friends joining (including you):\n"))
if num_friends <= 0:
    print("No one is joining for the party")
else:
    print("Enter the name of every friend (including you), each on a new line:")
    friends = {}
    for _ in range(num_friends):
        name = input()
        friends[name] = 0
    total_amount = int(input("Enter the total amount:\n"))

    split_amount = round(total_amount / num_friends, 2)

    for key in friends:
        friends[key] = split_amount