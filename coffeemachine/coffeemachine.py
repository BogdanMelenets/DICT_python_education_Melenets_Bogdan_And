print("Starting to make a coffee")
print("Grinding coffee beans")
print("Boiling water")
print("Mixing boiled water with crushed coffee beans")
print("Pouring coffee into the cup")
print("Pouring some milk into the cup")
print("Coffee is ready!")
mashin=[0, 0, 0]
#water, milk, beans
mashin[0]=int(input("Write how many ml of water the coffee machine has:"))
mashin[1]=int(input("Write how many ml of milk the coffee machine has:"))
mashin[2]=int(input("Write how many grams of coffee beans the coffee machine has:"))

cou=int(input("Write how many cups of coffee you will need:"))
water=200*cou
milk=50*cou
beans=15*cou
countcup=[0, 0, 0]
#water, milk, beans
if mashin[0]>=water and mashin[1]>=milk and mashin[2]>=beans:
    print ("Yes, I can make that amount of coffee.")
    if mashin[0] > water and mashin[1] > milk and mashin[2] > beans:
        countcup[0] = int(round((mashin[0]-water)/200,0))
        countcup[1]= int(round((mashin[1]-milk)/50, 0))
        countcup[2]= int(round((mashin[2]-beans)/15, 0))
        countcup.sort()
        print ("Yes, I can make that amount of coffee (and even", countcup[0], "more than that)")
if mashin[0]<water or mashin[1]<milk or mashin[2]<beans:
    countcup[0] = int(round(mashin[0] / 200, 0))
    countcup[1] = int(round(mashin[1] / 50, 0))
    countcup[2] = int(round(mashin[2] / 15, 0))
    countcup.sort()
    print("No, I can make only", countcup[0], "cups of coffee")



print("For", cou, "cups of coffee you will need:")
print (water, "ml of water")
print (milk, "ml of milk")
print (beans, "g of coffee beans")


