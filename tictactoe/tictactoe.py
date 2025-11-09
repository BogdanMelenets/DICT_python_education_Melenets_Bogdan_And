Pole=[['-', '-', '-', '-', '-'], ['|', '_', '_', '_', '|'], ['|', '_', '_', '_', '|'], ['|', '_', '_', '_', '|'], ['-', '-', '-', '-', '-']]
result=0
cherga='X'
while result==0:
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

    if err==0:
       if cherga=='X':
           Pole[int(inpoleX[0])][int(inpoleX[2])] = 'X'
           cherga = '0'
       else:
           Pole[int(inpoleX[0])][int(inpoleX[2])] = '0'
           cherga = 'X'
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
          if  win==1:
              print (Win," wins")
              result = 1
          if por==0 and Win in '1':
              print ("Draw")
              result = 1
       else:
          if win==0 and por==0:
              print ("Draw")
              result = 1
          if win==0 and por>0 and abs(countx-count0)<2: print ("Game not finished")
          else:
            print ("Impossible")
    else: print ("Error")