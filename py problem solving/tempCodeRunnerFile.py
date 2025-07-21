

total_bill=int(input("eneter a amount:"))
if total_bill<=1000:
    discount=0
    discount_amount=(total_bill*0)/100
elif total_bill<=5000:
    discount=10
    discount_amount=(total_bill*10)/100
elif total_bill<=10000:
    discount=20
    discount_amount=(total_bill*20)/100
else:
    discount=30
    discount_amount=(total_bill*30)/100

final_bill=total_bill-discount_amount
print("-----Final Bill---")
print(final_bill)