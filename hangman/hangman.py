import random
print ("HANGMAN")
print ("The game will be available soon.")
words=["python", "java", "javascript", "php"]
testword = random.choice (words)
str=("Guess the word: "+testword[:3])
len1 = len(testword)
i=0
while i<(len1-3):
    str = str + "-"
    i=i+1
str=str+">"
word=input (str)
if word==testword: print ("You survived!")
else: print ("You lost!")