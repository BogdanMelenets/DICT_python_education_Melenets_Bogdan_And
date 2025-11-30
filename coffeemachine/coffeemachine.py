class Cofmash:

  def __init__(self, water, milk, beans, cups, money, stan):
    self.water = water
    self.milk = milk
    self.beans = beans
    self.cups = cups
    self.money = money
    self.stan = stan

  def get_mashin(self):
      return f"stan: {self.stan}, water: { self.water } ml, milk:  {self.milk} ml, beans: {self.beans}, cups: {self.cups}, money: {self.money}"

  def get_work(self, vibor):
      # water, milk, beans, $
     if vibor=="buy":
         cup = [[250, 0, 16, 4], [350, 75, 20, 7], [200, 100, 12, 6]]
         print("1> еспресо")
         print("2> лате")
         print("3> капучіно")
         print("back> to main menu")
         vv = input("Enter your choice>")
         if vv != "back":
            v = int(vv) - 1
            if self.water >= cup[v][0] and self.milk >= cup[v][1] and self.beans >= cup[v][2] and self.cups > 0:
               self.water = self.water - cup[v][0]
               self.milk = self.milk - cup[v][1]
               self.beans = self.beans - cup[v][2]
               self.money = self.money + cup[v][3]
               self.cups = self.cups - 1
               self.stan = "Get coffee"
            else:
               self.stan = "I have enough resources, making you a coffee!"
         else:
             self.stan = "back"
     if vibor == "remaining":
          self.stan = "Availability output"
     if vibor == "take":
          self.stan = "Money has been issued"
          print("I gave you ", f"{mashin.get_money()}  $")
          self.money = 0
     if vibor == "fill":
          self.stan = "Ingredients added"
          print("Write how many ml of water you want to add:")
          self.water = self.water + int(input(">"))
          print("Write how many ml of milk you want to add:")
          self.milk = self.milk + int(input(">"))
          print("Write how many grams of coffee beans you want to add:")
          self.beans = self.beans + int(input(">"))
          print("Write how many disposable coffee cups you want to add:")
          self.cups = self.cups + int(input(">"))
     return

  def get_stan (self):
      return self.stan
  def get_money (self):
      return self.money
  def get_stan (self):
      return self.stan




mashin=Cofmash(400, 540, 120, 550, 9, "Ready")
print("The coffee machine has:")
print(mashin.get_mashin())
action=""
while action!="exit":
   action=input("Write action (buy, fill, take, remaining, exit):")
   i=(mashin.get_work(action))
   if mashin.get_stan() != "back":
       print("The coffee machine has:", mashin.get_mashin())





