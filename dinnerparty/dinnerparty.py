print("Enter the number of friends joining (including you):")
coun=input (">")
count = int(coun)
friends= {0: ""}
if count > 0:
    print("Enter the name of every friend (including you), each on a new line:")
    i=0
    while i < count:
        friends[i]=input(">")
        i=i+1
    for i in friends:
        print(friends[i])
else:
    print("No one is joining for the party")