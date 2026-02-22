class Cofmash:

  def __init__(self, water, milk, beans, cups, money, stan, cup, active_button):
    self.water = water
    self.milk = milk
    self.beans = beans
    self.cups = cups
    self.money = money
    self.stan = stan
    self.cup = cup
    self.active_button = active_button

  def get_mashin(self):
      return f"stan: {self.stan}, water: { self.water } ml, milk:  {self.milk} ml, beans: {self.beans}, cups: {self.cups}, money: {self.money}"

  def take(self):
      self.stan = "Money has been issued"
      ii = self.money
      self.money = 0
      return self.stan, f'I gave you : {ii} money, in mashin there are : {mashin.get_money()} money'

  def fill(self):
      self.stan = "Ingredients added"
      print("Write how many ml of water you want to add:")
      self.water = self.water + int(input(">"))
      print("Write how many ml of milk you want to add:")
      self.milk = self.milk + int(input(">"))
      print("Write how many grams of coffee beans you want to add:")
      self.beans = self.beans + int(input(">"))
      print("Write how many disposable coffee cups you want to add:")
      self.cups = self.cups + int(input(">"))
      return self.stan

  def getting_coffe(self):
      if self.water >= self.cup[int(self.active_button) - 1][0] and self.milk >= self.cup[int(self.active_button) - 1][1] and self.beans >= self.cup[int(self.active_button) - 1][2] and self.cups > 0:
          self.water = self.water - self.cup[int(self.active_button) - 1][0]
          self.milk = self.milk - self.cup[int(self.active_button) - 1][1]
          self.beans = self.beans - self.cup[int(self.active_button) - 1][2]
          self.money = self.money + self.cup[int(self.active_button) - 1][3]
          self.cups = self.cups - 1
          self.stan = "Get coffee"
      else:
          self.stan = "I have enough resources, making you a coffee!"
      return self.stan

  def buy(self):
      print("1> еспресо")
      print("2> лате")
      print("3> капучіно")
      print("back> to main menu")
      self.active_button = input("Enter your choice>")
      if self.active_button != "back": print(self.getting_coffe())
      else:
          self.stan = "back"
      return ""

  def get_stan (self):
      return self.stan

  def get_money (self):
      return self.money

  def get_stan (self):
      return self.stan

  def work(self):
      action = ""
      while action != "exit":
          action = input("Write action (buy, fill, take, remaining, exit):")
          if action == "buy": print(mashin.buy())
          if action == "remaining": self.stan = "Availability output"
          if action == "take": print(mashin.take())
          if action == "fill": print(mashin.fill())
          if mashin.get_stan() != "back":
              print("The coffee machine has:", mashin.get_mashin())
      return self.water, self.milk, self.beans, self.cups, self.money, self.stan



mashin=Cofmash(400, 540, 120, 550, 9, "Ready",  [[250, 0, 16, 4], [350, 75, 20, 7], [200, 100, 12, 6]], "")

print("___________________________________________________________________________________________________________")
print("At the beginning of work the coffee machine has:")
print(mashin.get_mashin())
print("___________________________________________________________________________________________________________")

print(mashin.work())

print("___________________________________________________________________________________________________________")
print("At the end of work the coffee machine has:")
print(mashin.get_mashin())