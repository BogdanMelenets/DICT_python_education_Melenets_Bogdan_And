import random
def rezult (a1, b1, o1, rez):
    res=""
    if o1=="+":
        if a1+b1==rez: res="Right!"
        else: res="Wrong!"
    if o1 == "-":
         if a1 - b1 == rez: res = "Right!"
         else: res = "Wrong!"
    if o1=="*":
        if a1*b1==rez:  res="Right!"
        else:   res="Wrong!"
    if o1=="/":
        if a1/b1==rez:  res="Right!"
        else:   res="Wrong!"
    if o1=="^2":
        if a1*a1==rez:  res="Right!"
        else:   res="Wrong!"
    if o1=="^3":
        if a1*a1*a1==rez:  res="Right!"
        else:   res="Wrong!"
    return res

def l_oper (level):
    i = 1
    n = 0
    while i < 6:
        if level=="1":
            op = random.choice(oper)
            a = random.randint(2, 9)
            b = random.randint(2, 9)
            print(a, op, b)
        if level=="2":
            op="^2"
            a = random.randint(11, 29)
            b=1
            print(f"{a}^2")
        if level=="3":
            op="^3"
            a = random.randint(1, 5)
            b=1
            print(f"{a}^3")
        korrect = 1
        while korrect == 1:
            rezp = input(">")
            try:
                print(rezult(a, b, op, int(rezp)))
                if rezult(a, b, op, int(rezp)) == "Right!": n = n + 1
                i = i + 1
                korrect = 0
            except ValueError:
                print("Incorrect format.")
    return n

oper=["+", "-", "*", "/"]
mm=1
while mm==1:
   print("Which level do you want? Enter a number:")
   print("1 - simple operations with numbers 2-9")
   print("2 - integral squares of 11-29")
   print("3 - raising to the third power of 1-5")
   menu = input(">")
   try:
       if int(menu) in [1, 3]:
          mm = 0
       else: print("Incorrect format.")
   except ValueError:
       print("Incorrect format.")
result=l_oper(menu)
print(f"Your mark is {result}/5")

fi=input("Would you like to save your result to the file? Enter yes or no.")
if fi in ["yes", "YES", "y", "Yes", "Y"]:
    Name=input ("Name>")
    if menu=="1": menu="1 - simple operations with numbers 2-9"
    if menu=="2": menu="2 - integral squares of 11-29"
    if menu == "3": menu = "3 - raising to the third power of 1-5"
    it=Name+": "+ str(result)+"/5 in level " +menu
    fi = input("Would you like to add your result in file? Enter yes to add or other symbol to rewrite.")
    if fi in ["yes", "YES", "y", "Yes", "Y"]:
         with open('results.txt', 'a') as f:
           f.write(f'{it}\n')
           f.close()
    else:
        with open('results.txt', 'w') as f:
            f.write(f'{it}\n')
            f.close()
