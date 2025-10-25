import random
print ("HANGMAN")
print ("The game will be available soon.")
words=["python", "java", "javascript", "php"]
wordspr=""
testword = random.choice (words)
print (testword)
len1 = len(testword)
i=0
strnew=""
sproba=1
while i < (len1):
    strnew = strnew + "-"
    i = i + 1

spr=1
while sproba<8:

   print("Спроба №", sproba)
   word=input ("Input a letter: >")
   posspr=wordspr.find(word[0])
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

   else:
       sproba = sproba + 1
       print("No improvements")
print(strnew)
if strnew==testword: print ("You survived!")
else: print("Thanks for playing! We'll see how well you did in the next stage")
