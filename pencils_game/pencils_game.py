import random
print("How many pencils would you like to use:")
err=0
ccells=0
while err==0:
    count=input(">")
    if count.isnumeric():
        err=1
        ccells = int(count)
    else: print ("The number of pencils should be numeric")
    if err==1 and count.startswith("-"):
        err=0
        print ("The number of pencils should be numeric")
    if err==1 and ccells==0:
        err=0
        print ("The number of pencils should be positive")
name=["Bob","Din"]
print("Who will be the first (", name[0], ",", name[1],"):")
err=0
while err==0:
    ncells=input(">")
    if ncells in name:
        err=1
    else: print("Choose between", name[0], ",", name[1])

cells=""
for i in range(ccells): cells=cells+"|"
print(cells)
print(ncells, "is going first!")
zalishok=ccells
if ncells==name[0]:
    first=0
    bot=1
else:
    first=1
    bot=0
while zalishok>0:
   print(name[first], "turn:")
   err = 0
   while err == 0:
       if first != bot :
          minusstr = input(">")
          if minusstr not in ["1", "2", "3"]: print("Possible values: '1', '2' or '3'")
          else:
             minus = int(minusstr)
             err=1
             if minus > zalishok:
                 err=0
                 print("Too many pencils were taken")
       else:
           err=1
           if zalishok > 25:  minus=random.randint(1, 3)
           else:
              if zalishok in [4, 8, 12, 16, 20, 24]: minus=3
              if zalishok in [3, 7, 11, 15, 19, 23]: minus = 2
              if zalishok in [2, 6, 10, 14, 18, 22]: minus = 1
              if zalishok==1:  minus=1
              if zalishok in [5, 9, 13, 17, 21, 25]: minus=random.randint(1, 3)
           print (minus)
   zalishok=zalishok-minus
   cells = ""
   for i in range(zalishok): cells = cells + "|"
   print(cells)
   if first==0: first=1
   else: first=0
print(name[first], "won!")