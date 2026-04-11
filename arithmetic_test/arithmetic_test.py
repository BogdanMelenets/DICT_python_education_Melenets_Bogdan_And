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
a=random.randint(2, 9)
b=random.randint(2, 9)
op=random.choice(oper)
print(a,op,b)
rezp=int(input (">"))

print (rezult(a, b,op,rezp))
