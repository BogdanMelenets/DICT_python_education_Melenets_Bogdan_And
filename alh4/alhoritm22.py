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
        Size1 = random.randint(25, 62)
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

st = Outerwear("Olko", "шуба", "синій", 40, "зима", "жіноча")
st1 = Outerwear("Olko", "шуба", "синій", 40, "літо", "чоловіча")
# print(st.get_info())
# print(st.get_message())
# print(st1.get_info())
# print(st1.get_message())
# print()
