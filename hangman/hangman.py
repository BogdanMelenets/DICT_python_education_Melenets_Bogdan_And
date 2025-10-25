import random
print ("HANGMAN")
print ("The game will be available soon.")
words=["python", "java", "javascript", "php"]
testword = random.choice (words)
print (testword)
len1 = len(testword)
i=0
strnew=""
sproba=0
while i < (len1):
    strnew = strnew + "-"
    i = i + 1


while sproba<8:
   sproba = sproba + 1
   print("Спроба №", sproba)
   word=input ("Input a letter: >")

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
   else: print("That letter doesn't appear in the word")
print(strnew)
if strnew==testword: print ("You survived!")
else: print("Thanks for playing! We'll see how well you did in the next stage")
