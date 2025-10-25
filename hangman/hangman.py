import random
print ("HANGMAN")
print ("The game will be available soon.")
words=["python", "java", "javascript", "php"]
wordspr=""
testword = random.choice (words)
vib=""
while vib not in ["play", "exit"]:
   print ("Type 'play' to play the game")
   print ("'exit' to quit")
   vib=input (": >")
if vib=="play":

   len1 = len(testword)
   i=0
   strnew=""
   sproba=1
   while i < (len1):
       strnew = strnew + "-"
       i = i + 1
   print(strnew)
   spr=1
   while sproba<9:

      print("Спроба №", sproba)
      word=input ("Input a letter: >")
      posspr=wordspr.find(word[0])
      if len(word)<2:
         if (word.islower()):
            if  posspr<0:
               wordspr = wordspr+word[0]
               Pos=testword.find(word)
               if  Pos>-1:
                   j=Pos
                   strnew=(strnew[:j]+word[0]+strnew[j+1:])
                   j=j+1
                   while j<(len1):
                      if testword[j]==word[0]:  strnew=(strnew[:j]+word[0])
                      else: strnew=(strnew[:j+1]+"-")
                      j = j + 1
                   strnew = (strnew[:len1])
                   print(strnew)
               else: sproba = sproba + 1;  print("That letter doesn't appear in the word")

            else: print("You've already guessed this letter.")
         else: print ("Please enter a lowercase English letter.")
      else:
          print("You should input a single letter.")

   print(strnew)
   if strnew==testword: print ("You survived!")
   else: print("Thanks for playing! We'll see how well you did in the next stage")
