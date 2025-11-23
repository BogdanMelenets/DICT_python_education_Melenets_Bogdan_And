def buy (mashn):
    # water, milk, beans, $
   cup=[[250, 0, 16, 4], [350, 75, 20, 7], [200, 100, 12, 6]]
   print ("1> еспресо")
   print ("2> лате")
   print ("3> капучіно")
   vv=input("Enter your choice>")
   if vv!="back":
      v=int()-1
      if mashn[0] >= cup[v][0] and mashn[1] >= cup[v][1] and mashn[2] >= cup[v][2] and mashn[4] >0:
          mashn[0] = mashn[0] - cup[v][0]
          mashn[1] = mashn[1] - cup[v][1]
          mashn[2] = mashn[2] - cup[v][2]
          mashn[3] = mashn[3] + cup[v][3]
          mashn[4] = mashn[4] - 1
          mashn[5] = 1
      else: mashn[5] = 0
   else:  mashn[5] = 2
   return mashn


def fill (mashin):
    print("Write how many ml of water you want to add:")
    mashin[0]=mashin[0]+int(input(">"))
    print("Write how many ml of milk you want to add:")
    mashin[1] = mashin[1] + int(input(">"))
    print("Write how many grams of coffee beans you want to add:")
    mashin[2] = mashin[2] + int(input(">"))
    print("Write how many disposable coffee cups you want to add:")
    mashin[4] = mashin[4] + int(input(">"))
    return mashin

def take (mashin):
    print("I gave you ", mashin[3])
    mashin[3]=0
    return mashin

# water, milk, beans, $, cups, result
mashin=[400, 540, 120, 550, 9, 1]
print("The coffee machine has:")
print(mashin[0], "of water")
print(mashin[1], " of milk")
print(mashin[2], " of coffee beans")
print(mashin[4], "of disposable cups")
print(mashin[3], " of money")
action=""
while action!="exit":
    action=input("Write action (buy, fill, take, remaining, exit):")
    if action=="buy":
       mashin=buy(mashin)
       if mashin[5]== 0: print ("I have enough resources, making you a coffee!")
       if mashin[5]== 2: action=""
    if action=="fill": mashin = fill (mashin)
    if action=="take": mashin = take (mashin)
    if action=="remaining":
       print("The coffee machine has:")
       print(mashin[0], "of water")
       print(mashin[1], " of milk")
       print(mashin[2], " of coffee beans")
       print(mashin[4], "of disposable cups")
       print(mashin[3], " of money")







