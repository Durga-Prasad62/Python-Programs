# total_liter=int(input("enter the liters:"))
# if total_liter<=50:
#     bill=total_liter*2
# elif total_liter<=150:
#     first_50lit=50*2
#     remaining=(total_liter-50)*3
#     bill=first_50lit+remaining
# else:
#     first_50lit=50*2
#     next_100lit=100*3
#     remaining=(total_liter-150)*5
#     bill=first_50lit+next_100lit+remaining

# print("-----: total bill is ------:")
# print(bill)



# distance=float(input("enter a distance:"))
# if distance<=3:
#     print("free")
# elif distance<=10:
#     print("delivary charge=10")
# elif distance<=20:
#     print("delivary charge=20")
# else:
#     print("Delivery not available")

# age=int(input("enter a age:"))
# if age<5:
#     print("free")
# elif age<=12:
#     print("rs=10")
# elif age<=60:
#     print("rs=20")
# else:
#     print("rs=5")


# marks=int(input("enter a marks:"))
# if marks<0 or marks>100:
#     print("invalid marks")
# elif marks>=90:
#     print("Grade:A")
# elif marks>=75:
#     print("Grade:B")
# elif marks>=60:
#     print("Grade:C")
# elif marks>=40:
#     print("Grade:D")
# else:
#     print("Fail")


# speed=int(input("enter a speed:"))
# if speed<=60:
#     print("no fine")
# elif speed<=80:
#     print("fine=100")
# elif speed<=100:
#     print("fine=200")
# else:
#     print("fine=500")


# hours=int(input("enter hours:"))
# if hours<=8:
#     print(100*hours)
# elif hours>8:
#     first8_hours=8*100
#     extra=150*(hours-8)
#     hours=first8_hours+extra
#     print(hours)



# withdrawel_Amount=int(input("enter a number"))
# if withdrawel_Amount<=500:
#     print("charge=10")
# elif withdrawel_Amount<=20000:
#     print("charge=20")
# else:
#     print("charge=50")




# unit=int(input("enter a unit:"))
# if unit<=100:
#     bill=unit*1
# elif unit<=200:
#     first_100=100*1
#     remaining=(unit-100)*2
#     bill=first_100+remaining
# else:
#     first_100=100*1
#     next_100=100*2
#     remaining=(unit-200)*3
#     bill=first_100+next_100+remaining
# print("---total bill---")
# print(bill)
  

# if bill>500:
#     print("---surcharge---")
#     bill=bill+(bill*15/100)
#     print(bill)



# total_bill=int(input("eneter a amount:"))
# if total_bill<=1000:
#     discount=0
#     discount_amount=(total_bill*0)/100
# elif total_bill<=5000:
#     discount=10
#     discount_amount=(total_bill*10)/100
# elif total_bill<=10000:
#     discount=20
#     discount_amount=(total_bill*20)/100
# else:
#     discount=30
#     discount_amount=(total_bill*30)/100

# final_bill=total_bill-discount_amount
# print("-----Final Bill---")
# print(final_bill)



# temperature=float(input("enter a temparature:"))
# if temperature<97:
#     print("Low")
# elif temperature<99:
#     print("Normal")
# elif temperature<101:
#     print("Mid Fever")
# else:
#     print("High Fever")

# # NESTED if-elif-else

# marks=int(input("enter a marks:"))
# if marks>=35:
#     if marks>=90:
#         print("Grade:A")
#     elif marks>=75:
#         print("Grade:B")
#     elif marks>=60:
#         print("Grade:C")
#     else:
#         print("Grade:D")
# else:
#     print("Fail")



# Total_bill=int(input("enter a amount:"))
# if Total_bill>0:
#     if Total_bill>10000:
#         discount=30
#     elif Total_bill>5000:
#         discount=20
#     else:
#         discount=10
#     discount_Amount=(Total_bill*discount/100)
#     if discount_Amount>=5000:
#         print("free delivery")
#         final_bill=Total_bill-discount_Amount
#         print(final_bill)

#     else:
#         print("Delivery charge:100")
#         final_bill=Total_bill-discount_Amount+100
#         print(final_bill)

# else:
#   print("Invalid bill")



# speed=int(input("enter a speed:"))
# License_type=input("Enter License Type:")
# if speed>60:
#     if License_type == 'Learner':
#         print("1000 rs fine")
#     elif License_type == 'Permanent':
#          print("500 rs fine")
#     else:
#         print("Unknown License Type")
# else:
#     print("no fine")


# unit=int(input("enter a unit:"))
# result = 0
# if unit<=100:
#     bill=unit*1
#     print(bill)
# elif unit<=200:
#     first_100=100*1
#     remaining=(unit-100)*2
#     bill=first_100+remaining
#     print(bill)
  
# else:
#     first_100=100*1
#     next_100=100*2
#     remaining=(unit-200)*3
#     bill=first_100+next_100+remaining
#     print(bill)
#     if bill>500:
#         surcharge=(bill*15)/100
#         print("surcharge",surcharge)


# age=int(input("enter  age"))
# time=input("enter Matinee or evening")
# if age<=5:
#     print("Free")                                                                  
# elif age<18:
#     if time=='matinee':
#         print("price:50rs")
#     else:
#         print("price:70rs")
# else:

#     if time=='matinee':
#         print("price:100rs")
#     else:
#         print("price:120")

# age=int(input("enter age:"))
# income=int(input("enter income:"))
# if age>=60:
#     if income<30000:
#         print("Eligible for benefits")
#     else:
#         print("Not eligible")
# else:
#     print("Not a senior citizen")


# vehicle_type=(input("enter a vehicle type-(2-wheeler/4-wheeler):"))
# fuel_type=input("enter a fuel type(petrol/diesel/electric):")
# if vehicle_type=='2-wheeler':
#     if fuel_type=='petrol':
#         print("10/L subsidy")
#     else:
#         print("No Subsidy")
# if vehicle_type=='4-wheeler':
#     print("No subsidy")


# total_bill=int(input("enter the bill:"))
# if total_bill>=500:
#     quality=input("quality of service( excellent,good):")
#     if quality=='excellent':
#         print(total_bill*10/100, "tip")
#     elif quality=='good': 
#         print(total_bill*5/100, "tip")
#     else:
#         print("No tip")
# else:
#     print("No tip")


# marks=int(input("enter  marks:"))
# if marks>=90:
#     income=int(input("enter family income:"))
#     if income<200000:
#         print("Full  Schlolarship")
#     else:
#         print("Grade A,No Scholarship")   
# elif marks>=75:
#     print("Grade B") 
# else:
#     print("No Scholarship")



# Employee_Type=input("enter the employee type-(Permanent/Contract)")
# years_of_Service=int(input("enter years of service"))
# if type=='Permanent':
#     if years_of_Service>=5:
#         print("bonus=5000rs")
# elif type=='Contract':
#     if years_of_Service>=5:
#         print("bonus=3000rs")
# else:
#     print("bonus=1000rs")




# age=int(input("enter age"))
# student_status=input("enter the status of the student")
# if age<5:
#     print("free ride")
# else:
#     if student_status=='yes':
#         print("5rs Fare")
#     else:
#         if age>60:
#             print("4rs  Fare")
#         else:
#             print("10rs Fare")




# gender=input("enter the gender type")
# age=int(input("enter age"))
# if gender=='Female':
#     if age>40:
#         print("30 % discount")
#     else:
#         print("20 % discount")
# elif gender=='male':
#     if age>40:
#         print("20 % discount")
#     else:
#         print("10 % discount")
# else:
#     print("Invalid Gender")



# income=int(input("enter Income"))
# cibil_score=int(input("enter cibil score"))
# if income>300000:
#     if cibil_score>=750:
#         print("Eligible for Loan")
#     else:
#         print("Not Eligible for loan(Low Cibil)")
# else:
#     print("not elible (Low Income)")


# data_usage=float(input("enter a data usage in GB"))
# network_type=(input("enter network type:(4G/5G):"))
# if data_usage<=2 :
#     if network_type=='5G':
#         print("50rs")
#     else:
#          print("30rs")
# else:
#     if network_type=='5G':
#         print("100rs")
#     else:
#           print("70rs")

# amount=int(input("enter amount"))
# day_type=input("enter weekday/weeekend")
# if amount>=5000:
#     if day_type=='weekend':
#         print("rs1000 voucher")
#     else:
#          print("rs500 voucher")
# else:
#     print("no offer")

# print('' and'prasad')




    




                                                         










