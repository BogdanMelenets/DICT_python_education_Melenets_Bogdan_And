Pole=[['-', '-', '-', '-', '-'], ['|', 'X', '0', '0', '|'], ['|', '0', 'X', '0', '|'], ['|', '0', 'X', 'X', '|'], ['-', '-', '-', '-', '-']]
inpole=input("Enter cells:")
inm=1
for i in range(len(inpole)):
    if inpole[i] not in ['0', 'X', '_', '-', '|']: inm=0
if (inm==1 and (len(inpole)==9)):
    Pole[1][1]=inpole[0]
    Pole[1][2] = inpole[1]
    Pole[1][3] = inpole[2]
    Pole[2][1] = inpole[3]
    Pole[2][2] = inpole[4]
    Pole[2][3] = inpole[5]
    Pole[3][1] = inpole[6]
    Pole[3][2] = inpole[7]
    Pole[3][3] = inpole[8]
    for i in range(len(Pole)):
       str=""
       for j in range(len(Pole)): str=str+Pole[i][j]
       print (str)

    inpoleX = input("Enter the coordinates:")
    err=1
    while err==1:
       if not (inpoleX[0]+inpoleX[2]).isdigit():
           print("You should enter numbers!")
       else:
          if Pole[int(inpoleX[0])][int(inpoleX[2])] in ['X', '0']:
              print ("This cell is occupied! Choose another one!")
          else:
             if inpoleX[0] not in ['1', '2', '3'] or inpoleX[2] not in ['1', '2', '3']:
                 print("Coordinates should be from 1 to 3!")
             else: err=0
       if err==1: inpoleX = input("Enter the coordinates:")
    if err == 0:
        Pole[int(inpoleX[0])][int(inpoleX[2])] = 'X'
        for i in range(len(Pole)):
            str = ""
            for j in range(len(Pole)): str = str + Pole[i][j]
            print(str)

    else: print ("Error")