def ci(p,r,t):
   
    a = p* (pow((1+r/100), t))
    CI= a-p
    print("compound interest is", CI)

ci(10000,10.25,5)
def compound_interest(principal, rate, time):
 
    # Calculates compound interest
    Amount = principal * (pow((1 + rate / 100), time))
    CI = Amount - principal
    print("Compound interest is", CI)
 
 
# Driver Code
compound_interest(10000, 10.25, 5)