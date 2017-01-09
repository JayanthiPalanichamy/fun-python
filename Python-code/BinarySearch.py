balance=float(raw_input("Enter the outstanding balance on your credit card:"))
interestRate=float(raw_input("Enter the annual credit card interest rate as a decimal :"))
Minpayment=0.0;
MonRate=interestRate/12.0
f=0
lwBound=balance/12.0
upBound=(balance*(1+(interestRate/12.0))**12.0)/12.0
nwbalance=(lwBound+upBound)/2.0
while nwbalance>0:
    count=0
    Minpayment +=10.0
    nwbalance=balance
    for i in range(0,12):
        nwbalance =nwbalance*(1+MonRate)-Minpayment
        count=count+1
        if nwbalance<=0:
            break
        
nwbalance=round(nwbalance,2)   
print "RESULT\nMonthly payment to pay off debt in 1 year:",Minpayment,"\nNumber of months needed:",count,"\nBalance:",nwbalance
