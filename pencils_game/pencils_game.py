print("How many pencils would you like to use:")
ccells=int(input(">"))
print("Who will be the first (Bob, Din):")
ncells=input(">")
cells=""
for i in range(ccells): cells=cells+"|"
print (cells)
print(ncells, "is going first!")