class Outerwear:
   Brand: str # виробник одягу
   Type: str # тип одягу
   Color: str # кольор одягу
   Size: int # розмір одягу
   Season: str # сезон одягу
   Category: str # носій одягу


   def __init__(self, Brand, Type, Color, Size, Season, Category):
# Конструктор класу - метод, що запускається при створенні об'єкта
# і використовується для початкового внесення необхідних даних"""
     self.Brand = Brand
     self.Type = Type
     self.Color = Color
     self.Size = Size
     self.Season = Season
     self.Category = Category



   def get_info(self):
      return f'Товар: {self.Type}, бренду {self.Brand}, кольору {self.Color}, розміру {self.Size}, категорії  {self.Category}'

   def get_message (self):
     if self.Type=="шуба" and self.Category != "жіноча" and self.Category != "дитяча" : self.Season = " "
     else:
         if self.Type == "дублянка" and self.Category != "жіноча" and self.Category != "дитяча":
             self.Season = " "
         else:
             if self.Type == "пуховик":
                 self.Season = "Зима"
             else:
                 if self.Type == "шуба":
                     self.Season = "Зима"
                 else:
                     if self.Type == "дублянка":
                         self.Season = "Зима"
                     else:
                         if self.Type == "куртка":
                             self.Season = "Всі сезони"
                         else:
                             self.Season = "Усі окрім літа"
     if self.Season == " ": return f'Нажаль {self.Type}, бренду {self.Brand} немає в наявності'
     else:
         return f'Обраний: {self.Type}, бренду: {self.Brand}, розміром: {self.Size}, відноситься до "{self.Season}" колекції'


st = Outerwear("Olko", "шуба", "синій", 40, "", "чоловіча")
print(st.get_info())
print(st.get_message())
print()
st = Outerwear("Zara", "дублянка", "чорний", 52, "", "чоловіча")
print(st.get_info())
print(st.get_message())
print()
st = Outerwear("Nike", "пуховик", "чорний", 46, "", "дитяча")
print(st.get_info())
print(st.get_message())
print()
st = Outerwear("Adidas", "пальто", "сірий", 42, "", "жіноча")
print(st.get_info())
print(st.get_message())
print()
st = Outerwear("Fila", "куртка", "жовтий", 46, "", "жіноча")
print(st.get_info())
print(st.get_message())
print()
st = Outerwear("Olko", "шуба", "синій", 40, "", "жіноча")
print(st.get_info())
print(st.get_message())
print()
st = Outerwear("Ferro", "дублянка", "білий", 38, "", "дитяча")
print(st.get_info())
print(st.get_message())
print()
st = Outerwear("Bugatti", "куртка", "червоний", 56, "", "чоловіча")
print(st.get_info())
print(st.get_message())