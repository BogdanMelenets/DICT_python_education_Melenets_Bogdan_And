import random
print ("HANGMAN")
print ("The game will be available soon.")
words=["python", "java", "javascript", "php"]
testword = random.choice (words)
word=input ("Guess the word: >")
if word==testword: print ("You survived!")
else: print ("You lost!")