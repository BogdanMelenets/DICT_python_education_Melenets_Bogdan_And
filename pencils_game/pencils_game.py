print("How many pencils would you like to use:")
ccells=int(input(">"))
name=["Bob","Din"]
print("Who will be the first (", name[0], ",", name[1],"):")
ncells=input(">")
cells=""
for i in range(ccells): cells=cells+"|"
print(cells)
print(ncells, "is going first!")
zalishok=ccells
if ncells==name[0]: first=0
else: first=1
while zalishok>0:
   print(name[first], "turn:")
   minus = int(input(">"))
   zalishok=zalishok-minus
   cells = ""
   for i in range(zalishok): cells = cells + "|"
   print(cells)
   if first==0: first=1
   else: first=0