#if aplicant has high income and good credit score 
#   eligible for loan or else decline loan

income= 40000
good_credit= 10

if income > 50000 and good_credit > 7:
    print("YOUR ELIGIBLE FOR LOAN")
elif income <=20000 and good_credit>=4:
    print("YOUR SCORE OR ELIGIBLE ARE LOW TRY TO INCREASE ")
else:
    print("YOUR NOT ELIGIBLE FOR LOAN")