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
    # порожні комірки та Х та 0
    por = 0
    countx = 0
    count0 = 0
    for i in range(len(Pole)):
       for j in range(len(Pole)):
            if Pole[i][j] in '_': por = 1 + por
            if Pole[i][j] in 'X': countx = 1 + countx
            if Pole[i][j] in '0': count0 = 1 + count0
    Win='1'
    win=0


    #строка
    for i in range(len(Pole)):
       if Pole[i][1]=='X' and Pole[i][2]=='X' and Pole[i][3]=='X':
           Win='X'
           win=win+1
       if Pole[i][1]=='0' and Pole[i][2]=='0' and Pole[i][3]=='0':
           Win='0'
           win = win + 1
    #рядок
    for i in range(len(Pole)):
        if Pole[1][i] == 'X' and Pole[2][i] == 'X' and Pole[3][i] == 'X':
            Win = 'X'
            win = win + 1
        if Pole[1][i] == '0' and Pole[2][i] == '0' and Pole[3][i] == '0':
            Win='0'
            win = win + 1
    #діагональ
    if Pole[1][1] == 'X' and Pole[2][2] == 'X' and Pole[3][3] == 'X':
        Win='X'
        win = win + 1
    if Pole[1][3] == 'X' and Pole[2][2] == 'X' and Pole[3][1] == 'X':
        Win='X'
        win = win + 1
    if Pole[1][1] == '0' and Pole[2][2] == '0' and Pole[3][3] == '0':
        Win='0'
        win = win + 1
    if Pole[1][3] == '0' and Pole[2][2] == '0' and Pole[3][1] == '0':
        Win = '0'
        win = win + 1
    if win==1 and abs(countx-count0)<2:
       if por>0 and Win in '1': print ("Game not finished")
       if Win not in '1': print (Win," wins")
       if por==0 and Win in '1': print ("Draw")
    else:
       if win==0 and por==0:  print ("Draw")
       if win==0 and por>0 and abs(countx-count0)<2: print ("Game not finished")
       else:
          print ("Impossible")
else: print ("Error")