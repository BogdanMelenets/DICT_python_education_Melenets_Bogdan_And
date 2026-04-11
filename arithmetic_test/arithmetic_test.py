import random
def rezult (a1, b1, o1, rez):
    res=""
    if o1=="+":
        if a1+b1==rez: res="Right!"
        else: res="Wrong!"
    if o1 == "-":
         if a1 - b1 == rez: res = "Right!"
         else: res = "Wrong!"
    if o1=="*":
        if a1*b1==rez:  res="Right!"
        else:   res="Wrong!"
    return res

oper=["+", "-", "*"]
i=1
n=0
while i<6:
  a=random.randint(2, 9)
  b=random.randint(2, 9)
  op=random.choice(oper)
  print(a,op,b)
  korrect=1
  while korrect == 1:
    rezp=input (">")
    try:
      print(rezult(a, b, op, int(rezp)))
      if rezult(a, b, op, int(rezp)) == "Right!": n = n + 1
      i = i + 1
      korrect = 0
    except ValueError:
      print("Incorrect format.")
print(f"Your mark is {n}/5")
