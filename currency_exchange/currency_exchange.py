mycoins = float(input("Please, enter the number of mycoins you have: "))
rate = float(input("Please, enter the exchange rate: "))

dollars = mycoins * rate

print(f"The total amount of dollars: {dollars:.2f}")

mycoins = float(input())

ars_rate = 0.82
hnl_rate = 0.17
aud_rate = 1.9622
mad_rate = 0.208

print(f"I will get {round(mycoins * ars_rate, 2)} ARS from the sale of {mycoins} mycoins.")
print(f"I will get {round(mycoins * hnl_rate, 2)} HNL from the sale of {mycoins} mycoins.")
print(f"I will get {round(mycoins * aud_rate, 2)} AUD from the sale of {mycoins} mycoins.")
print(f"I will get {round(mycoins * mad_rate, 2)} MAD from the sale of {mycoins} mycoins.")