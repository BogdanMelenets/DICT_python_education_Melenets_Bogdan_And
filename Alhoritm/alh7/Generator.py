import random

class Generator:
    Brand = ("Olko","Zara","Nike","Adidas","Fila","Ferro","Bugatti")
    Type = ("шуба", "дублянка", "пуховик", "пальто", "куртка")
    Color = ("синій", "чорний", "сірий", "жовтий", "синій", "білий", "червоний")
    Size : int
    Season = ("літо", "зима", "демісезон")
    Category = ["чоловіча", "жіноча", "дитяча"]

    def generate_max (self) -> Outerwear:
        """Метод автоматичного створення екземпляру класу Outerwear з  випадковими чи обраними з певного переліку значеннями кожної
        властивості класу   """
        Brand1 = "я"
        Type1 = "я"
        Color1 = "я"
        Size1 = 0
        Season1 = "я"
        Category1 = "я"
        return Outerwear(Brand1, Type1, Color1, Size1, Season1, Category1)

    def generate_single (self) -> Outerwear:
        """Метод автоматичного створення екземпляру класу Outerwear з  випадковими чи обраними з певного переліку значеннями кожної
        властивості класу   """
        Brand1 = random.choice(self.Brand)
        Type1 = random.choice(self.Type)
        Color1 = random.choice(self.Color)
        Size1 = random.randint(1, 10001)
        Season1 = self.Season[random.randint(0, 2)]
        Category1 = self.Category [random.randint(0, 2)]
        return Outerwear (Brand1, Type1, Color1, Size1, Season1, Category1)

    def generate_1000(self) -> list:
        """Метод генерування 1000 об'єктів класу Outerwear"""
        plist = list()
        for i in range(1000):
            plist.append(self.generate_single())
        return plist


    def generate_10_000(self) -> list:
     """Метод генерування 10 000 об'єктів"""
     plist = [self.generate_single() for i in range(10000)]
     return plist
    pass

class Outerwear:
   Brand: str # виробник одягу
   Type: str # тип одягу
   Color: str # кольор одягу
   Size: int # розмір одягу
   Season: str # сезон одягу
   Category: str # носій одягу

   def __init__(self, Brand: str, Type: str, Color: str, Size: int, Season: str, Category: str )-> None:
# Конструктор класу - метод, що запускається при створенні об'єкта
# і використовується для початкового внесення необхідних даних"""
     self.Brand = Brand
     self.Type = Type
     self.Color = Color
     self.Size = Size
     self.Season = Season
     self.Category = Category

   def __repr__(self):
       return f"Outerwear({self.Type}, {self.Brand}, {self.Color}, {self.Size}, {self.Category})"

   def get_Type(self)-> str:
       return self.Type

   def get_Size(self)-> int:
       return self.Size

   def get_info(self)-> str:
      return f'Товар: {self.Type}, бренду {self.Brand}, кольору {self.Color}, розміру {self.Size}, категорії  {self.Category}'

   def get_message(self):
       if self.Type == "шуба" and self.Category != "жіноча" and self.Category != "дитяча":
           self.Season = " "
       else:
           if self.Type == "дублянка" and self.Category != "жіноча" and self.Category != "дитяча":
               self.Season = " "
           else:
               if self.Type == "пуховик":
                   self.Season = "зима"
               else:
                   if self.Type == "шуба":
                       self.Season = "зима"
                   else:
                       if self.Type == "дублянка":
                           self.Season = "зима"
                       else:
                           if self.Type == "куртка":
                               self.Season = "демісезон"
                           else:
                               self.Season = "демісезон"
       if self.Season == " ":
         mes = f'Нажаль {self.Type}, бренду {self.Brand} немає в наявності'
       else:
         mes = f'Обраний: {self.Type}, бренду: {self.Brand}, розміром: {self.Size}, відноситься до "{self.Season}" колекції'
       return mes

def rndstr(N):
    g = Generator()
    g5 = [g.generate_single() for i in range(N)]
    return g5

def strbezpovt(N):
    g = Generator()
    g5 = [g.generate_single() for i in range(N)]
    i = 1
    while i < N:
        g1 = g.generate_single()
        povt = 0
        for j in range(i):

            if g5[j].get_Size() == g1.get_Size(): povt = 1
        if povt == 0: g5[i] = g1
        i = i + 1
    return g5

   # Сортування масиву за розміром одягу
def poradok(mas):
    MasSize = len(mas)
    g = Generator()
    groboch = [[] for i in range(MasSize)]
    max = 1
    indmax = 0
    irob = 0
    while irob < MasSize:
        i = 0
        while i < MasSize:
            if mas[i].get_Size() > max:
                indmax = i
                max = mas[i].get_Size()
            i = i + 1
        groboch[irob] = mas[indmax]
        max = mas[indmax].get_Size()
        mas[indmax] = g.generate_max()
        max = 1
        irob = irob + 1
    return groboch

def Lenght(s):
    N = 0
    for item in s: N = N + 1
    return N

def Getitem(s, pos):
    return s[pos]

def Getit(str, el, L):
    res = 0
    for j in range(L):
        if str[j] == el: res = j
    return res

def Count(St, data):
    N = 0
    for item in St:
        if item == data: N = N + 1
    return N

def Reverse(St):
    N = Lenght(St)
    g = Generator()
    res = [g.generate_single() for i in range(N)]
    i = 0
    for item in St:
        res[N - i - 1] = item
        i = i + 1
    return res



st = Outerwear("Olko", "шуба", "синій", 40, "зима", "жіноча")
st1 = Outerwear("Olko", "шуба", "синій", 40, "літо", "чоловіча")

print()