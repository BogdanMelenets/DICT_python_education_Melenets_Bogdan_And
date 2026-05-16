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