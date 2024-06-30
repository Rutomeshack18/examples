#!/bin/bash
#Calculating discounts based on different prices
purchase_amount= float(input("Enter purchase amount: "))
if purchase_amount>= 1000:
    discount= 0.1 #10% discount
elif purchase_amount>=500:
    discount= 0.05 #5% discount
else:
    discount= 0 # no discount
final_price= purchase_amount*(1-discount)
print("Your final price is: $ "+str(final_price))
