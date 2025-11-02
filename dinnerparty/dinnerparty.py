import random
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
    for Fr, value in friends.items():
        print(f'{Fr}: {value}')
    print("Enter the total amount")
    su = input(">")
    sum = float(su)
    sumone=round(sum/(count + 1), 2)
    for i in friends:
        friends[i]=sumone
    for Fr, value in friends.items():
        print(f'{Fr}: {value}')
    print("Do you want to use the 'Who is lucky?' feature? Write Yes/No:")
    luc=input (">")
    if luc=="Yes":
        ii=random.randint(0, count-1)
        jj=0
        for Fr, value in friends.items():
            if jj==ii:
                 print(f'{Fr}', "is the lucky one!")
            jj=jj+1
    else:
        print("No one is going to be lucky.")
else:
    print("No one is joining for the party")