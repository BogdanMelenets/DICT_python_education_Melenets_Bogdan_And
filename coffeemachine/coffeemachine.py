def buy (mashin):
    # water, milk, beans, $
   cup=[[250, 0, 16, 4], [350, 75, 20, 7], [200, 100, 12, 6]]
   print ("1> еспресо")
   print ("2> лате")
   print ("3> капучіно")
   v=int(input("Enter your choice>"))-1
   if mashin[0] >= cup[v][0] and mashin[1] >= cup[v][1] and mashin[2] >= cup[v][2] and mashin[4] >0:
       mashin[0] = mashin[0] - cup[v][0]
       mashin[1] = mashin[1] - cup[v][1]
       mashin[2] = mashin[2] - cup[v][2]
       mashin[3] = mashin[3] + cup[v][3]
       mashin[4] = mashin[4] - 1
   return mashin

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
    mashin[3]=0
    return mashin

# water, milk, beans, $, cups
mashin=[400, 540, 120, 550, 9]
print("The coffee machine has:")
print(mashin[0], "of water")
print(mashin[1], " of milk")
print(mashin[2], " of coffee beans")
print(mashin[4], "of disposable cups")
print(mashin[3], " of money")

action=input("Write action (buy, fill, take):")
if action=="buy": mashin = buy (mashin)
if action=="fill": mashin = fill (mashin)
if action=="take": mashin = take (mashin)


print("The coffee machine has:")
print(mashin[0], "of water")
print(mashin[1], " of milk")
print(mashin[2], " of coffee beans")
print(mashin[4], "of disposable cups")
print(mashin[3], " of money")







