import math
import argparse
import sys

class CustomArgumentParser(argparse.ArgumentParser):
    def error(self, message):
        # Дія замість стандартного виклику sys.exit(2)
        print(f"Incorrect parameters: {message}", file=sys.stderr)
        sys.exit(2)


# 1. Створюємо парсер
parser = CustomArgumentParser(description="Парсер з помилкою")

# 2. Додаємо аргументи
parser.add_argument("--type", type=str, required=True, choices=["diff", "annuity"], help="Type")
parser.add_argument("--principal", type=int, help="Principal")
parser.add_argument("--periods", type=int, help="Periods")
parser.add_argument("--interest", type=int, required=True, help="Interest")
parser.add_argument("--payment", type=int, help="Payment")

# 3. Парсимо аргументи
args = parser.parse_args()

if args.type=="diff":
    if args.principal==None or args.periods==None:
        print(f"Incorrect parameters" )
        sys.exit(2)
if args.type=="annuity":
    CountParam=0
    if args.principal!=None: CountParam=CountParam+1
    if args.periods!=None: CountParam=CountParam+1
    if args.payment!=None: CountParam=CountParam+1
    if CountParam<2:
        print(f"Incorrect parameters" )
        sys.exit(2)

# 4. Переносимо аргументи в змінні
type = args.type
principal = args.principal
periods = args.periods
interest = args.interest
payment=args.payment

def annuit (Type, Sum, MonthCount, Loan, Monthpay):
    result=['']
    if Type == 'n':
        NomLoan=(Loan/(12*100))
        MontsCount=round(math.log(Monthpay/(Monthpay-NomLoan*Sum), (1+NomLoan))+0.5)
        YearCount=round(MontsCount/12-0.5)
        LastMonthCount=MontsCount-YearCount*12
        result[0] = 'It will take '
        if YearCount>0: result[0]= result[0]+str(YearCount)+' years'
        if LastMonthCount>0:
            if YearCount > 0: result[0] = result[0] + " and "
            result[0]=result[0] + str(LastMonthCount)+ " months to repay this loan!"
    if Type=='a':
        NomLoan = (Loan / (12 * 100))
        MonthPay=(Sum*(NomLoan*math.pow((1+NomLoan), MonthCount)))/(math.pow((1+NomLoan),MonthCount) -1)
        result[0]= "Your monthly payment = "+str(round(MonthPay+0.5))+"!"
        AllSum=0
        for i in range(1, MonthCount+1):
            AllSum=AllSum+round(MonthPay+0.5)
        result.append("")
        result.append("Overpayment = " + str(round(AllSum - Sum)))

    if Type == 'p':

        NomLoan = (Loan / (12 * 100))
        Sum = Monthpay / ((NomLoan * math.pow((1 + NomLoan), MonthCount))/ (math.pow((1 + NomLoan), MonthCount) - 1))
        result[0]="Your loan principal ="+str (round(Sum))+"!"
    return result

def diff (Sum, MonthCount, Loan):
        result = ['']
        NomLoan = (Loan / (12 * 100))
        AllSum=0
        for i in range(1, MonthCount+1):
            Dm=round(Sum/MonthCount+NomLoan*(Sum-(Sum*(i-1)/MonthCount))+0.5)
            AllSum=AllSum+Dm
            result.append ("Month "+str(i)+" : payment is "+str(Dm))
        result.append("")
        result.append ("Overpayment = "+str(round(AllSum-Sum)))
        return result




if type == "diff": print('\n'.join(diff(principal, periods, interest)))
if type=="annuity":
    if payment==None: print('\n'.join(annuit("a", principal, periods, interest, 0)))
    if periods==None: print('\n'.join(annuit("n", principal, 0, interest, payment)))
    if principal==None: print('\n'.join(annuit("p", 0, periods, interest, payment)))

