import math
"""
def rozrah(Sum, Type):
    result="Error"
    if Type == 'm':
        paymonth=int(input("Enter the monthly payment:"))
        result="It will take "+str(round(Sum/paymonth)+0.5)+" months to repay the loan"
    if Type == 'p':
        paymonth = int(input("Enter the number of months:"))
        payment=round(Sum/(paymonth)+0.5)
        lastpayment = Sum-(paymonth-1) * payment
        result="Your monthly payment = "+ str(payment) +" and the last payment = "+ str(lastpayment)
    return result


pochsum = int(input("Enter the loan principal:"))
print("What do you want to calculate?")
print('type "m" – for number of monthly payments,')
print('type "p" – for the monthly payment:')
print(rozrah(pochsum, input('>')))
"""

def rozrah(Type):
    result="Error"
    if Type == 'n':
        print("Enter the loan principal:")
        Sum=int(input(">"))
        print("Enter the monthly payment:")
        Monthpay = int(input(">"))
        print("Enter the loan interest:")
        Loan = float(input(">"))
        NomLoan=(Loan/(12*100))
        MontsCount=round(math.log(Monthpay/(Monthpay-NomLoan*Sum), (1+NomLoan))+0.5)
        YearCount=round(MontsCount/12-0.5)
        LastMonthCount=MontsCount-YearCount*12
        result = "It will take "
        if YearCount>0: result= result+str(YearCount)+" years"
        if LastMonthCount>0:
            if YearCount > 0: result = result + " and "
            result=result + str(LastMonthCount)+ " months to repay this loan!"
    if Type=='a':
        print("Enter the loan principal:")
        Sum = int(input(">"))
        print("Enter the number of periods:")
        MonthCount = int(input(">"))
        print("Enter the loan interest:")
        Loan = float(input(">"))
        NomLoan = (Loan / (12 * 100))
        MonthPay=(Sum*(NomLoan*math.pow((1+NomLoan), MonthCount)))/(math.pow((1+NomLoan),MonthCount) -1)
        result= "Your monthly payment = "+str(round(MonthPay+0.5))+"!"
    if Type == 'p':
        print("Enter the annuity payment:")
        MonthPay = float(input(">"))
        print("Enter the number of periods:")
        MonthCount = int(input(">"))
        print("Enter the loan interest:")
        Loan = float(input(">"))
        NomLoan = (Loan / (12 * 100))
        Sum = MonthPay / ((NomLoan * math.pow((1 + NomLoan), MonthCount))/ (math.pow((1 + NomLoan), MonthCount) - 1))
        result="Your loan principal ="+str (round(Sum))+"!"
    return result

print("What do you want to calculate?")
print('type "n" for number of monthly payments,')
print('type "a" for annuity monthly payment amount,')
print('type "p" for loan principal:')
print(rozrah(input('>')))