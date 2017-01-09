#A program to compute Total amount of interest paid on credit card and the remaining balance to be paid

balance=float(raw_input("Enter the outstanding balance on your credit card: "))
AnnualInterest=float(raw_input("Enter the annual credit card interest rate as a decimal: "))
MinRate=float(raw_input("Enter the minimum monthly payment rate as a decimal: "))
totAmt=0
for i in range(1,13):
    monthpay=round(MinRate*balance,2)
    interestAmt=round(AnnualInterest/12.0*balance,2)
    principalPaid=round(monthpay-interestAmt,2)
    balance -=principalPaid
    totAmt +=interestAmt+principalPaid
    print "Month:%d\nMinimum monthly payment:$%.2f\nPrinciple paid:$%.2f\nRemaining balance:$%.2f"%(i,monthpay,principalPaid,balance)
print "RESULT\nTotal Amount paid:$",totAmt,"\nRemaining Balance :$",balance

    
                     
                        
