print("Enter the number of friends joining (including you):")
coun=input (">")
count = int(coun)
friends= {}
if count > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    i=0
    while i < count:
        fr=input(">")
        friends.update({fr :0})
        i=i+1
    print(friends.items())
    print("Enter the total amount")
    su = input(">")
    sum = float(su)
    sumone=round(sum/(count + 1), 2)
    for i in friends:
        friends[i]=sumone
    print(friends.items())

else:
    print("No one is joining for the party")