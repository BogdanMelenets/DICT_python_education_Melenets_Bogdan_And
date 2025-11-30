import random
# побудова слова з прочерків
def procherk (ww):
    new=""
    i=0
    len1 = len(ww)
    while i < (len1):
        new = new + "-"
        i = i + 1
    return new

#аналіз помилок
def pomilka(w, wo): # w - символ уведений з клавіатури, wo - слово з прочерків та літер, що вгадується
    pomilk = 10
    if len(w) != 1: pomilk = 0 # введено більше одного символа
    if not w.islower(): pomilk = 1 # введено велику літеру
    if wo.find(w[0]) > -1 : pomilk = 2 #така літера уже вводилась
    return pomilk

# заміна символа у строці
def zamin (stroka, position, symb):
    original_string = stroka
    # Перетворюємо строку на список символів
    list_of_str = list(original_string)
    # Змінюємо символ з індексом Pos на уведений символ
    list_of_str[Pos] = symb
    # Об'єднуємо список назад у строку
    stroka = "".join(list_of_str)
    return stroka


print ("HANGMAN")
print ("The game will be available soon.")
words=["python", "java", "javascript", "php"]
errors=["You should input a single letter", "Please enter a lowercase English letter.", "You've already guessed this letter."]
testword = random.choice (words) # слово яке необхідно вгадати
etalon=testword # зберігаємо шукане слово у ще одній змінній оскільки testword буде змінюватись
vib=""
while vib not in ["play", "exit"]:
   print ("Type 'play' to play the game")
   print ("'exit' to quit")
   vib=input (": >")
if vib=="play":
   strnew = procherk (testword) # будуємо слово з прочерків
   print(strnew)
   sproba=1
   while sproba<9:
      print("Спроба №", sproba)
      word=input ("Input a letter: >")
      #  перевіраємо на помилки
      if pomilka(word, strnew) != 10: print (errors[pomilka(word, strnew)])
      else:
          Pos=testword.find(word) # номер позиції букви з клавіатури у слові, що потрібно вгадати
          if Pos == -1 : sproba = sproba + 1;  print("That letter doesn't appear in the word") # якщо буква відсутня у слові
          else: # якщо буква наявна у слові
              while Pos != -1: # опрацьовуємо випадок коли буква уведена з клавіатури зутрічається понад 1 раз у слові
                  # у строці символів замінюємо - на букву з клавіатури
                  strnew= zamin (strnew, Pos, word)
                  # замінюємо на " " букву уведену з клавіатури у шуканому слові, щоб вийти з циклу
                  testword = zamin (testword, Pos, " ")
                  Pos = testword.find(word)
                  if strnew == etalon:
                      print("You survived!")
                      # змінюємо змінні щоб вийти з циклу оскільки слово вже вгадане
                      Pos = -1
                      sproba = 10
      print(strnew)
   if strnew != etalon: print("Thanks for playing! We'll see how well you did in the next stage")
