import numpy as np

def tax(income):
    if income<=300000:
        tax_pay=0
    elif income<=700000:
        tax_pay=float(0.20*(income-300000))
    else:
        tax_pay=float(0.20*400000+0.35*(income-700000))

    return tax_pay

tax_p=tax(100000)
print(tax_p)

    
 



    