from copy import deepcopy

from alhoritm22.alhoritm22 import Generator
from alhoritm22.alhoritm22 import Outerwear
from alh3.Abstr import AbstractStructureBasic, AbstractStructureExtended
from Strexampl import StructureExample
import time

# Завдання 1
def rndstr(N):
  g = Generator()
  g5 = [g.generate_single() for i in range(N)]
  return g5

def strbezpovt(N):
    g = Generator()
    g5=[[] for i in range(N)]
    i=1
    g5[0]=g.generate_single()
    while i<N :
        g1=g.generate_single()
        povt=0
        for j in range(i):
            if g5[j]==g1: povt=1
        if povt==0: g5[i]=g1
        i=i+1
    return g5

# Сортування масиву за розміром одягу
def poradok(mas):
    MasSize=len(mas)
    g = Generator()
    groboch = [[] for i in range(MasSize)]
    max=1
    indmax=0
    irob=0
    while irob<MasSize:
      i=0
      while i<MasSize:
        if mas[i].get_Size()>max:
            indmax=i
            max=mas[i].get_Size()
        i = i + 1
      groboch[irob] = mas[indmax]
      max=mas[indmax].get_Size()
      mas[indmax]=g.generate_max()
      max=1
      irob=irob+1
    return groboch

def Lenght (s):
    N=0
    for item in s: N=N+1
    return N

def Getitem (s, pos):
    return s[pos]

def Setitem (s, d, pos):
    s[pos]=d
    return s

def Append (sa, d, N):
    g=Generator()
    res = [g.generate_single() for i in range(N)]
    j=0
    while j<N-1:
        res[j] = sa[j]
        j=j+1
    res[j]=d
    return res

def Insert(str, vstavka, pos, Len):
    g = Generator()
    res = [g.generate_single() for i in range(Len+1)]
    j = 0
    while j < Len:
        if j==pos:
            res[j] = vstavka
            j=j+1
            res[j] = str[j]
        else:
            res[j] = str[j]
            j=j+1

    return res

def Getit (str, el, L):
    res=0
    for j in range(L):
        if str[j] == el: res=j
    return res

def Remove(str, el, L):
    g = Generator()
    res = [g.generate_single() for i in range(L-1)]
    j = 0
    jj = 0
    while j < L:
        if str[j] == el:
            j = j + 1
        else:
            res[jj] = str[j]
            j = j + 1
            jj=jj+1

    return res

def Delit (str, Pos, L):
    g = Generator()
    res = [g.generate_single() for i in range(L-1)]
    j = 0
    jj = 0
    while j < L:
        if j == Pos:
           j = j + 1
        else:
            res[jj] = str[j]
            j = j + 1
            jj=jj+1
    return res

def Copy (St):
    g = Generator()
    res = [g.generate_single() for i in range(Lenght(St))]
    N = 0
    for item in St:
        res[N] = item
        N = N + 1
    return res


def Extend (St, data):
    g = Generator()
    res = [g.generate_single() for i in range(Lenght(St)+Lenght(data))]
    N = 0
    for item in St:
        res[N] = item
        N = N + 1
    for item in data:
        res[N] = item
        N = N + 1
    return res

def Count (St, data):
    N = 0
    for item in St:
        if item==data: N=N+1
    return N

def Reverse (St):
    N = Lenght(St)
    g = Generator()
    res = [g.generate_single() for i in range(N)]
    i=0
    for item in St:
        res[N-i-1]=item
        i=i+1
    return res

def Mul (St, Povt):
    N = Lenght(St)*Povt
    g = Generator()
    res = [g.generate_single() for i in range(N)]
    i=0
    while i<N:
       for item in St:
          res[i]=item
          i=i+1
    return res

def CopyD (St, L):
    g = Generator()
    res = [g.generate_single() for i in range(L)]
    N = 0
    while N<L:
        res[N] = St[N]
        N = N + 1
    return res


def Min (St):
    min = St[0]
    for item in St:
        if min>item: min=item
    return min

def Max (St):
    max = St[0]
    for item in St:
        if max<item: max=item
    return max

def rozrah (mm):
    ll=int(input("Введіть кількість елементів структури>"))
    g = Generator()
    if mm=="1": g5=rndstr(ll)
    if mm=="2": g5=strbezpovt(ll)
    if mm=="3":
        mmm=strbezpovt(ll)
        g5=poradok([g.generate_single() for i in range(ll)])
    lst = g5
    tpl = tuple(g5)
    s1 = StructureExample(tpl)
    s3 = StructureExample(tpl)
    s1.__init__(StructureExample(tpl))
    s3.__init__(StructureExample(tpl))
    gp1 = lst.copy()
    Len = Lenght(s1)
    print("Перелік і зміст елементів структури у вигляді рядка:", s1.__repr__())
    print (" ")

    mu = " "
    while mu != "q":
        print("________________________________________________________________________________________________________________________________________________________________________")
        print("|1  - len |    |2  - getitem|    |3  - setitem|   |4  - append|    |5  - insert|    |6  - getitem|    |7  - remove|    |8  - iter, next|    |9  - delitem|    |10 - pop|")
        print("|11 - copy|    |12 - clear  |    |13 - extend |   |14 - add   |    |15 - count |    |16 - reverse|    |17 - mul   |    |18 - deepcopy  |    |19 - min    |    |20 - max|")
        print("|q - вихід|                                                                                                                                                            |")
        print("________________________________________________________________________________________________________________________________________________________________________")
        mu = input()
        if mu == "1":
           print ("_____len__()________")
           start = time.time()
           print("Кількість елементів структури:", s1.__len__())
           end = time.time()
           T = end - start
           print("Час виконання:", T, " секунд")
           print("_____власна реалізація:________")
           start1 = time.time()
           Len = Lenght(s1)
           print("Кількість елементів структури:", Len)
           end1 = time.time()
           T1 = end1 - start1
           print("Час виконання:", T1, " секунд")
           print(f"Різниця", T - T1, " секунд")
           print(" ")
        if mu == "2":
            print("_______getitem__()________")
            start = time.time()
            N = int(input("Введіть індекс елемента у структурі>"))
            start = time.time()
            print("Значення ", N, "елемента структури: ", s1.__getitem__(N))
            end = time.time()
            T = end - start
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            print("Значення ", N, "елемента структури: ", Getitem(s1, N))
            end1 = time.time()
            T1 = end1 - start1
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
            print(" ")
        if mu == "3":
            print("_________setitem___()________")
            s3 = s1
            N = int(input("Введіть індекс елемента у структурі, який ви хочете замінити>"))
            gp = g.generate_single()
            print("Елемент буде замінено на:", gp)
            start = time.time()
            s1.__setitem__(N, gp)
            end = time.time()
            T = end - start
            print("Елементи:", s1)
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            print("Елементи:", Setitem(s3, gp, N))
            end1 = time.time()
            T1 = end1 - start1
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
            if mm == "3":
                s1 = poradok(s1)
                print("Перелік і зміст елементів після заміни та впорядкування:", s1)
            print(" ")
        if mu == "4":
            print("_________append()________")
            gp = g.generate_single()
            print("Буде додано елемент:", gp)
            start = time.time()
            s1.append(gp)
            end = time.time()
            T = end - start
            print("Елементи:", s1)
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            print("Елементи:", Append(s1, gp, Len))
            end1 = time.time()
            T1 = end1 - start1
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
            if mm == "3":
                s1 = poradok(s1)
                print("Перелік і зміст елементів після додавання та впорядкування:", s1)
            print(" ")
        if mu == "5":
            print("_________insert()________")
            N = int(input("Введіть, у яку позицію вставити елемент>"))
            gp = g.generate_single()
            print("Буде вставлено елемент:", gp)
            start = time.time()
            s1.insert(N, gp)
            end = time.time()
            T = end - start
            print("Перелік і зміст елементів після вставлення:", s1)
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            s1 = Insert(s1, gp, N, Len)
            print("Перелік і зміст елементів після вставлення:", s1)
            end1 = time.time()
            T1 = end1 - start1
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
            if mm == "3":
                s1 = poradok(s1)
                print("Перелік і зміст елементів після вставлення та впорядкування:", s1)
        if mu == "6":
            print("__________getitem__________")
            start = time.time()
            gp = s1.__getitem__(1)
            print("Елемент", gp, "знаходиться на позиції", s1.index(gp))
            end = time.time()
            T = end - start
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            print("Елемент", gp, "знаходиться на позиції", Getit(s1, gp, Len))
            end1 = time.time()
            T1 = end1 - start1
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
        if mu == "7":
            print("__________remove__________")
            print("Елементи:", s1)
            gp = s1.__getitem__(1)
            print("Буде вилучено елемент:", gp)
            start = time.time()
            s1.remove(gp)
            end = time.time()
            T = end - start
            print("Перелік і зміст елементів після вилучення:", s1)
            print("Час виконання:", T, " секунд")
            s1.insert(1, gp)
            print("_____власна реалізація:________")
            print("Буде вилучено елемент:", gp)
            start1 = time.time()
            s1 = Remove(s1, gp, Len)
            print("Перелік і зміст елементів після вилучення:", s1)
            end1 = time.time()
            T1 = end1 - start1
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
        if mu == "8":
            gp = lst.__iter__()
            print("Об'єкт-ітератор", gp)
            gp = s3.__next__()
            print("Наступний елемент  структури", gp)
            print("___________________")
        if mu == "9":
            print("__________delitem__________")
            print("Елементи:", lst)
            gp = lst.copy()
            N = int(input("Введіть, з якої позиції видалити елемент>"))
            start = time.time()
            lst.__delitem__(N)
            end = time.time()
            T = end - start
            print("Перелік і зміст елементів після видалення:", lst)
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            gp = Delit(gp, N, Len)
            end1 = time.time()
            T1 = end1 - start1
            print("Перелік і зміст елементів після видалення:", gp)
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
        if mu == "10":
            print("__________pop__________")
            print("Елементи:", lst)
            gp = lst.copy()
            N = int(input("Введіть, з якої позиції видалити елемент>"))
            start = time.time()
            lst.pop(N)
            end = time.time()
            T = end - start
            print("Перелік і зміст елементів після видалення:", lst)
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            gp = Delit(gp, N, Len)
            end1 = time.time()
            T1 = end1 - start1
            print("Перелік і зміст елементів після видалення:", gp)
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
        if mu == "11":
            print("________copy()_________")
            start = time.time()
            gp = lst.copy()
            end = time.time()
            T = end - start
            print("Копія структури", gp)
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            gp = Copy(lst)
            end1 = time.time()
            T1 = end1 - start1
            print("Копія структури", gp)
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
        if mu == "12":
            print("________clear()_________")
            gp = lst.copy()
            start = time.time()
            lst.clear()
            end = time.time()
            T = end - start
            print("Перелік і зміст елементів після видалення всіх елементів структури:", lst)
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            gp = []
            end1 = time.time()
            T1 = end1 - start1
            print("Перелік і зміст елементів після видалення всіх елементів структури:", gp)
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
            lst = gp1.copy()
        if mu == "13":
            print("________extend_________")
            start = time.time()
            lst = gp1.copy()
            g6 = [g.generate_single() for i in range(2)]
            print("Буде додано структуру", g6)
            lst.extend(g6)
            end = time.time()
            T = end - start
            print("Структура після додавання елементів", lst)
            print("Час виконання:", T, " секунд")
            lst = gp1.copy()
            print("_____власна реалізація:________")
            start1 = time.time()
            lst = Extend(lst, g6)
            end1 = time.time()
            T1 = end1 - start1
            print("Структура після додавання елементів", lst)
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
            lst = gp1.copy()
            if mm == "3":
                lst = poradok(lst)
                print("Перелік і зміст елементів після додавання та впорядкування:", lst)
        if mu == "14":
            print("________add_________")
            lst = gp1.copy()
            g6 = [g.generate_single() for i in range(2)]
            print("Буде додано структуру", g6)
            start = time.time()
            dd = lst.__add__(g6)
            end = time.time()
            T = end - start
            print("Структура після додавання елементів", dd)
            print("Час виконання:", T, " секунд")
            lst = gp1.copy()
            print("_____власна реалізація:________")
            start1 = time.time()
            lst = Extend(lst, g6)
            end1 = time.time()
            T1 = end1 - start1
            print("Структура після додавання елементів", lst)
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
            lst = gp1.copy()
            if mm == "3":
                dd = poradok(dd)
                print("Перелік і зміст елементів після додавання та впорядкування:", dd)
        if mu == "15":
            print("________count_________")
            print("Структура: ", lst)
            g6 = lst[0]
            start = time.time()
            print("Кількість входжень елемента ", g6, "у структуру", lst.count(g6))
            end = time.time()
            T = end - start
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            print("Кількість входжень елемента ", g6, "у структуру", Count(lst, g6))
            end1 = time.time()
            T1 = end1 - start1
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
        if mu == "16":
            print("_______reverse()________")
            gp1 = lst.copy()
            print("Перелік і зміст елементів до реверсу:", lst)
            start = time.time()
            lst.reverse()
            end = time.time()
            T = end - start
            print("Перелік і зміст елементів після реверсу:", lst)
            print("Час виконання:", T, " секунд")
            lst = gp1.copy()
            print("_____власна реалізація:________")
            start1 = time.time()
            print("Перелік і зміст елементів після реверсу:", Reverse(lst))
            end1 = time.time()
            T1 = end1 - start1
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
        if mu == "17":
            print("_______mul________")
            g6 = [g.generate_single() for i in range(2)]
            print("Cтруктурa", g6)
            N = int(input("Введіть, кількість дублювань>"))
            start = time.time()
            dd = g6.__mul__(N)
            end = time.time()
            T = end - start
            print("Структура після дублювання елементів", dd)
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            print("Структура після дублювання елементів", Mul(g6, N))
            end1 = time.time()
            T1 = end1 - start1
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
            if mm == "3":
                dd = poradok(dd)
                print("Перелік і зміст елементів після дублювання та впорядкування:", dd)
        if mu == "18":
            print("________deepcopy_________")
            start = time.time()
            gp = deepcopy(s1)
            end = time.time()
            T = end - start
            print("Копія структури", gp)
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            gp = CopyD(s1, Len)
            end1 = time.time()
            T1 = end1 - start1
            print("Копія структури", gp)
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
        if mu == "19":
            print("________min_________")
            grob = [s1[i].get_Size() for i in range(s1.__len__())]
            start = time.time()
            dd = min(grob)
            end = time.time()
            T = end - start
            print("Найменший елемент структури", dd)
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            ddd = Min(grob)
            end1 = time.time()
            T1 = end1 - start1
            print("Найменший елемент структури", ddd)
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
        if mu == "20":
            print("________max_________")
            grob = [s1[i].get_Size() for i in range(s1.__len__())]
            start = time.time()
            dd = max(grob)
            end = time.time()
            T = end - start
            print("Найбільший елемент структури", dd)
            print("Час виконання:", T, " секунд")
            print("_____власна реалізація:________")
            start1 = time.time()
            ddd = Max(grob)
            end1 = time.time()
            T1 = end1 - start1
            print("Найбільший елемент структури", ddd)
            print("Час виконання:", T1, " секунд")
            print(f"Різниця", T - T1, " секунд")
    return


menu=" "
while menu!="4":
  print ("1 - випадковий масив")
  print ("2 - масив без дублікатів")
  print ("3 - впорядкований масив")
  print ("4 - вихід")
  menu = input()
  if menu in ["1", "2", "3"]: print (rozrah(menu))


