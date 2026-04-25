from alhoritm22 import Generator
from alhoritm22 import Outerwear
# from Abstr import AbstractStructureBasic, AbstractStructureExtended
import time
import random

class Node:
    data: Outerwear
    next: None

    def __init__(self,initdata):
        self.data = initdata
        self.next = None


    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext

class DoubleNode:
    data: Outerwear
    next: None | DoubleNode = None
    prev: None | DoubleNode = None


    def __init__(self,initdata):
        self.data = initdata
        self.next = None
        self.prev = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self, newdata):
        self.data = newdata

    def setNext(self, newnext):
        self.next = newnext

    def getPrev(self):
        return self.prev

    def setPrev(self, newprev):
        self.prev = newprev

    def getSize(self):
        return self.data.Size

class UnorderedList:
        data: Outerwear

        def __init__(self,initdata):
            self.head = None
            self.data = initdata
            self.next = None

        def add(self, item):
            temp = Node(item)
            temp.setNext(self.head)
            self.head = temp


        def Urepr (self):
            Ul = self.head
            g = Generator()
            i=0
            res = [g.generate_single() for i in range(self.Ulen())]
            while Ul != None:
                res[i]=Ul.getData()
                Ul = Ul.getNext()
                i=i+1
            return res

        def No_Double(self, Len):
            Ul = self.head
            res=0
            i=1
            while i<Len:
                item=Ul.getData()
                j=i+1
                Ur=Ul.getNext()
                while j<Len:
                    if Ur.getData() == item:
                        g = Generator()
                        Zamina = UnorderedList(g.generate_single())
                        Zamina.add(g.generate_single())
                        Ul = Ul.Usetitem(Zamina, j)
                    j=j+1
                    Ur=Ur.getNext()
                i=i+1
                Ul = Ul.getNext()

            return

        # Сортування за розміром одягу
        def poriadok(self, Len):
            i=1
            mas=[[] for i in range(Len)]
            Ul=self.head
            j = 0
            while j < Len-1:
                i = 0
                Ul = self.head
                while i < Len - 1:

                    if Ul.getData().get_Size() < Ul.getNext().getData().get_Size():
                        rr=Ul.getData()
                        Ul.setData(Ul.getNext().getData())
                        Ul.getNext().setData(rr)
                    Ul = Ul.getNext()
                    i = i + 1

                j = j + 1

            return



        def Ulen(self):
            Ul = self.head
            count = 0
            while Ul != None:
                count = count + 1
                Ul = Ul.getNext()
            return count

        def Ugetitem(self, inde):
            Ul = self.head
            i = 1
            while i<inde:
              i=i+1
              Ul = Ul.getNext()
            return Ul

        def Urevers(self):
            Uw = self.head
            g = Generator()
            Ur = UnorderedList(g.generate_single())
            while Uw != None:
                Ur.add(Uw.getData())
                Uw = Uw.getNext()
            return Ur

        def Usetitem(self, item, index):
            Uw = self.head
            g = Generator()
            Ur = UnorderedList(g.generate_single())
            i=1

            while Uw != None:
                if i==index: Ur.add(item.Ugetitem(1).getData())
                else: Ur.add(Uw.getData())
                Uw = Uw.getNext()
                i=i+1
            Ur=Ur.Urevers()

            return Ur

        def Uinsert(self, item, index):
            Uw = self.head
            g = Generator()
            Ur = UnorderedList(g.generate_single())
            i=1
            while Uw != None:
                if i==index:
                    Ur.add(item.Urepr()[0])
                    Ur.add(Uw.getData())
                else: Ur.add(Uw.getData())
                Uw = Uw.getNext()
                i=i+1
            Ur=Ur.Urevers()
            return Ur

        def Uremove(self, index):
            Uw = self.head
            g = Generator()
            Ur = UnorderedList(g.generate_single())
            i=1
            while Uw != None:
                if i==index: Uw = Uw.getNext()
                else:
                    Ur.add(Uw.getData())
                    Uw = Uw.getNext()
                i=i+1
            Ur=Ur.Urevers()
            return Ur

        def Uindex(self, val, start, stop):
            Ul = self.head
            i=0
            indexU = 0
            while i<start-1:
              i=i+1
              Ul = Ul.getNext()
            while i<stop:
                i = i + 1

                if Ul.getData() == val:
                    indexU = i
                    i=stop+1
                Ul = Ul.getNext()

            return indexU

class OrderedList:
    data: Outerwear

    def __init__(self, initdata):
        self.head = None
        self.tail = None
        self.size = 0
        self.data = initdata
        self.next = None
        self.prev = None

    def add(self, item, iteration):

        if iteration==1 :self.tail = self.head
        temp = DoubleNode(item)
        self.prev=temp
        temp.prev = self.tail
        temp.next = self.head
        self.head = temp
        self.size = self.size + 1

        return




    def Orepr(self):
        Ul = self.head
        Len = self.size
        g = Generator()
        i = 0
        res = [g.generate_single() for i in range(self.Olen())]
        while i < Len:
            res[i] = Ul.getData()
            Ul = Ul.getNext()
            i = i + 1

        return res

    def Olen(self):
        return self.size

    def Orevers(self):
        Uw = self.head
        g = Generator()
        Ur = OrderedList(g.generate_single())
        i=1
        while Uw != None:
            Ur.add(Uw.getData(), i)
            i=i+1
            Uw = Uw.getNext()
        return Ur

    def Ogetitem(self, inde):
        Len = self.size
        if inde==Len: Ul=self.tail
        else:
            Ul = self.head
            i = 1
            while i < inde:
                i = i + 1
                Ul = Ul.getNext()
        return Ul

    def Osetitem(self, item, index):
        Uw = self.head
        Len=self.size
        g = Generator()
        Or = OrderedList(g.generate_single())
        i = 1

        while i <= Len:
            if i == index:
                Or.add(item.Orepr()[0], i)

            else:
                Or.add(Uw.getData(), i)
            Uw = Uw.getNext()
            i = i + 1
        Or = Or.Orevers()
        #  print (Ur)
        #  print (Ur.Urepr())
        return Or

    def Oinsert(self, item, index):
        Uw = self.head
        g = Generator()
        Ur = OrderedList(g.generate_single())
        i = 1
        while Uw != None:
            if i == index:
                Ur.add(item.Orepr()[0], i)
                Ur.add(Uw.getData(), i+1)
            else:
                Ur.add(Uw.getData(), i)
            Uw = Uw.getNext()
            i = i + 1
        Ur = Ur.Orevers()
        return Ur

    def Oindex(self, val, start, stop):
        Ul = self.head
        i = 0
        indexU = 0
        while i < start - 1:
            i = i + 1
            Ul = Ul.getNext()
        while i < stop:
            i = i + 1

            if Ul.getData() == val:
                indexU = i
                i = stop + 1
            Ul = Ul.getNext()

        return indexU

    def Oremove(self, index):
        Uw = self.head
        g = Generator()
        Ur = OrderedList(g.generate_single())
        i = 1
        while Uw != None:
            if i == index:
                Uw = Uw.getNext()
            else:
                Ur.add(Uw.getData(), i)
                Uw = Uw.getNext()
            i = i + 1
        Ur = Ur.Orevers()
        return Ur


def rozrah(mm):
    ll = int(input("Введіть кількість елементів списку>"))
    g = Generator()
    if mm in ["1", "2", "3"]:
         Unlist = UnorderedList(g.generate_single())

         for i in range(ll): Unlist.add(g.generate_single())
         if mm=="2": Unlist.No_Double(Unlist.Ulen())
         if mm=="3": Unlist.poriadok(Unlist.Ulen())
    if mm in ["4", "5", "6"]:
        Onlist = OrderedList(g.generate_single())
        for i in range(ll):  Onlist.add(g.generate_single(), i)


    mu = " "
    while mu != "q":
        print(
            "_____________________________________________________________________________________________________________________________________________")
        print(
            "|1  - len |    |2  - repr|    |3  - getitem|   |4  - setitem|    |5  - append|    |6  - insert|    |7  - index|    |8  - remove|   |q - вихід|")
        print(
            "______________________________________________________________________________________________________________________________________________")
        mu = input()
        if mu == "1":
            print("_____len__()________")
            start = time.time()
            if mm in ["1", "2", "3"]: print("Кількість елементів списку:", Unlist.Ulen())
            if mm in ["4", "5", "6"]: print("Кількість елементів списку:", Onlist.Olen())
            end = time.time()
            T = end - start
            print("Час виконання:", T, " секунд")
            print(" ")

        if mu == "2":
            print("_____repr__()________")
            start = time.time()
            if mm in ["1", "2", "3"]: print("Перелік і зміст елементів списку:", Unlist.Urepr())
            if mm in ["4", "5", "6"]: print("Перелік і зміст елементів списку:", Onlist.Orepr())
            end = time.time()
            T = end - start
            print("Час виконання:", T, " секунд")
            print(" ")

        if mu == "3":
            print("_____getitem__()________")
            try:
               ind=int(input("Введіть індекс елемента списку:"))
               if mm in ["1", "2", "3"]:
                   if ind > 0 and ind <= Unlist.Ulen():
                       print("Перелік і зміст елементів списку:", Unlist.Urepr())
                       start = time.time()
                       Un = Unlist.Ugetitem(ind)
                       print(f"{ind} елемент списку>", Un.getData())
                       end = time.time()
                       T = end - start
                       print("Час виконання:", T, " секунд")
                       print(" ")
                   else:
                       print("IndexError.")
               if mm in ["4", "5", "6"]:

                  if ind > 0 and ind <= Onlist.Olen():
                       print("Перелік і зміст елементів списку:", Onlist.Orepr())
                       start = time.time()
                       print(f"{ind} елемент списку>", Onlist.Ogetitem(ind).data)
                       end = time.time()
                       T = end - start
                       end = time.time()
                       T = end - start
                       print("Час виконання:", T, " секунд")
                       print(" ")
                  else:
                      print("IndexError.")
            except ValueError:
                print("Incorrect format.")

        if mu == "4":
            print("______setitem__(key)________")

            try:
                if mm in ["1", "2", "3"]:
                    print("Перелік і зміст елементів списку:", Unlist.Urepr())
                    ind = int(input("Введіть індекс елемента списку:"))
                    g = Generator()
                    Zamina = UnorderedList(g.generate_single())
                    Zamina.add(g.generate_single())
                    print(f"{ind}-ий елемент списку буде замінено на {Zamina.Urepr()}")
                    if ind > 0 and ind <= Unlist.Ulen():
                        start = time.time()
                        Unlist = Unlist.Usetitem(Zamina, ind)
                        if mm == "2":
                            Unlist.No_Double(Unlist.Ulen())
                            print("Перелік і зміст елементів списку після заміни та вилучення дублів:", Unlist.Urepr())
                        if mm == "3":
                            Unlist.poriadok(Unlist.Ulen())
                            print("Перелік і зміст елементів списку після заміни та впорядкування:", Unlist.Urepr())
                        if mm == "1":  print("Перелік і зміст елементів списку після заміни:", Unlist.Urepr())

                        end = time.time()
                        T = end - start
                        print("Час виконання:", T, " секунд")
                        print(" ")
                    else:
                        print("IndexError.")
                if mm in ["4", "5", "6"]:
                    print("Перелік і зміст елементів списку:", Onlist.Orepr())
                    ind = int(input("Введіть індекс елемента списку:"))
                    g = Generator()
                    Zamina = OrderedList(g.generate_single())
                    Zamina.add(g.generate_single(), 1)
                    print(f"{ind}-ий елемент списку буде замінено на {Zamina.Orepr()}")
                    if ind > 0 and ind <= Onlist.Olen():
                       start = time.time()
                       Onlist = Onlist.Osetitem(Zamina, ind)
                       print("Перелік і зміст елементів списку після заміни:", Onlist.Orepr())

                       end = time.time()
                       T = end - start
                       print("Час виконання:", T, " секунд")
                       print(" ")
                    else:
                      print("IndexError.")
            except ValueError:
                print("Incorrect format.")

        if mu == "5":
            print("_____append()________")
            if mm in ["1", "2", "3"]:
                g = Generator()
                item = g.generate_single()
                item = UnorderedList(g.generate_single())
                print("Перелік і зміст елементів списку:", Unlist.Urepr())
                print("Буде додано елемент>", item.data)
                start = time.time()
                Unlist = Unlist.Urevers()
                Unlist.add(item.data)
                Unlist = Unlist.Urevers()
                if mm == "2":
                    Unlist.No_Double(Unlist.Ulen())
                    print("Перелік і зміст елементів списку після додавання та вилучення дублів:", Unlist.Urepr())
                if mm == "3":
                    Unlist.poriadok(Unlist.Ulen())
                    print("Перелік і зміст елементів списку після додавання та впорядкування:", Unlist.Urepr())
                if mm == "1":  print("Перелік і зміст елементів списку після додавання:", Unlist.Urepr())

                end = time.time()
                T = end - start
                print("Час виконання:", T, " секунд")
                print(" ")
            if mm in ["4", "5", "6"]:
                g = Generator()
                item = g.generate_single()
                item = OrderedList(g.generate_single())
                print("Перелік і зміст елементів списку:", Onlist.Orepr())
                print("Буде додано елемент>", item.data)
                start = time.time()
                start = time.time()
                Onlist = Onlist.Orevers()
                Onlist.add(item.data, 1)
                Onlist = Onlist.Orevers()
                print("Перелік і зміст елементів списку після додавання:", Onlist.Orepr())
                end = time.time()
                T = end - start
                print("Час виконання:", T, " секунд")
                print(" ")
        if mu == "6":
            print("______insert(index, value)________")
            if mm in ["1", "2", "3"]:
                print("Перелік і зміст елементів списку:", Unlist.Urepr())
                try:
                    ind = int(input("Введіть індекс елемента списку перед яким буде додавання:"))
                    g = Generator()
                    Zamina = UnorderedList(g.generate_single())
                    Zamina.add(g.generate_single())
                    print(f"Перед {ind}-им елементом списку буде додано {Zamina.Urepr()}")
                    if ind > 0 and ind <= Unlist.Ulen():
                        start = time.time()
                        Unlist = Unlist.Uinsert(Zamina, ind)
                        if mm == "2":
                            Unlist.No_Double(Unlist.Ulen())
                            print("Перелік і зміст елементів списку після додавання та вилучення дублів:",
                                  Unlist.Urepr())
                        if mm == "3":
                            Unlist.poriadok(Unlist.Ulen())
                            print("Перелік і зміст елементів списку після додавання та впорядкування:", Unlist.Urepr())
                        if mm == "1":  print("Перелік і зміст елементів списку після додавання:", Unlist.Urepr())
                        end = time.time()
                        T = end - start
                        print("Час виконання:", T, " секунд")
                        print(" ")
                    else:
                        print("IndexError.")
                except ValueError:
                    print("Incorrect format.")
            if mm in ["4", "5", "6"]:
                print("Перелік і зміст елементів списку:", Onlist.Orepr())
                try:
                    ind = int(input("Введіть індекс елемента списку перед яким буде додавання:"))
                    g = Generator()
                    Zamina = OrderedList(g.generate_single())
                    Zamina.add(g.generate_single(), 1)
                    print(f"Перед {ind}-им елементом списку буде додано {Zamina.Orepr()}")
                    if ind > 0 and ind <= Onlist.Olen():
                        start = time.time()
                        Onlist = Onlist.Oinsert(Zamina, ind)
                        if mm == "4":  print("Перелік і зміст елементів списку після додавання:", Onlist.Orepr())
                        end = time.time()
                        T = end - start
                        print("Час виконання:", T, " секунд")
                        print(" ")
                    else:
                        print("IndexError.")
                except ValueError:
                    print("Incorrect format.")

        if mu == "7":
            print("______index(value, start, stop)________")
            if mm in ["1", "2", "3"]:
                print("Перелік і зміст елементів списку:", Unlist.Urepr())
                a = random.randint(1, Unlist.Ulen())
                value = Unlist.Ugetitem(a)
                print(f"Буде здійснено пошук елемента> {value.data}")
                try:
                    ind1 = int(input("Введіть початковий індекс елемента для пошуку:"))
                    ind2 = int(input("Введіть  кінцевий  індекс елемента для пошуку:"))
                    if ind1 > 0 and ind1 <= Unlist.Ulen() and ind2 > 0 and ind2 <= Unlist.Ulen() and ind1 <= ind2:
                        start = time.time()
                        rr = Unlist.Uindex(value.data, ind1, ind2)
                        if rr != 0:
                            print("Елемент знайдено за індексом:", rr)
                        else:
                            print("IndexError. (Element not foud)")
                        end = time.time()
                        T = end - start
                        print("Час виконання:", T, " секунд")
                        print(" ")
                    else:
                        print("IndexError.")
                except ValueError:
                    print("Incorrect format.")
            if mm in ["4", "5", "6"]:
                print("Перелік і зміст елементів списку:", Onlist.Orepr())
                a = random.randint(1, Onlist.Olen())
                value = Onlist.Ogetitem(a)
                print(f"Буде здійснено пошук елемента> {value.data}")
                try:
                    ind1 = int(input("Введіть початковий індекс елемента для пошуку:"))
                    ind2 = int(input("Введіть  кінцевий  індекс елемента для пошуку:"))
                    if ind1 > 0 and ind1 <= Onlist.Olen() and ind2 > 0 and ind2 <= Onlist.Olen() and ind1 <= ind2:
                        start = time.time()
                        rr = Onlist.Oindex(value.data, ind1, ind2)
                        if rr != 0:
                            print("Елемент знайдено за індексом:", rr)
                        else:
                            print("IndexError. (Element not foud)")
                        end = time.time()
                        T = end - start
                        print("Час виконання:", T, " секунд")
                        print(" ")
                    else:
                        print("IndexError.")
                except ValueError:
                    print("Incorrect format.")

        if mu == "8":
            print("______remove(index)________")
            if mm in ["1", "2", "3"]:
                print("Перелік і зміст елементів списку:", Unlist.Urepr())
                try:
                    ind = int(input("Введіть індекс елемента списку, який потрібно вилучити:"))
                    if ind > 0 and ind <= Unlist.Ulen():
                        start = time.time()
                        Unlist = Unlist.Uremove(ind)
                        print("Перелік і зміст елементів списку після вилучення:", Unlist.Urepr())

                        end = time.time()
                        T = end - start
                        print("Час виконання:", T, " секунд")
                        print(" ")
                    else:
                        print("IndexError.")
                except ValueError:
                    print("Incorrect format.")
            if mm in ["4", "5", "6"]:
                print("Перелік і зміст елементів списку:", Onlist.Orepr())
                try:
                    ind = int(input("Введіть індекс елемента списку, який потрібно вилучити:"))
                    if ind > 0 and ind <= Onlist.Olen():
                        start = time.time()
                        Onlist = Onlist.Oremove(ind)
                        print("Перелік і зміст елементів списку після вилучення:", Onlist.Orepr())

                        end = time.time()
                        T = end - start
                        print("Час виконання:", T, " секунд")
                        print(" ")
                    else:
                        print("IndexError.")
                except ValueError:
                    print("Incorrect format.")

    return




menu=" "
while menu!="5":
  print ("1 - Однозв’язний список")
  print ("2 - Однозв’язний список без дублікатів ")
  print ("3 - Впорядкований однозв’язний список")
  print ("4 - Двозв’язний список")
  print ("5 - вихід")
  menu = input()
  if menu in ["1", "2", "3", "4"]: print (rozrah(menu))