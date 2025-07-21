# units=float(input("enter a units:"))
# if units<=100:
#     bill=units*0
# elif units<=200:
#     first_100=100*0
#     remaining=(units-100)*5
#     bill=first_100+remaining
# else:
#     first_100=100*0
#     second_100=100*5
#     remaining=(units-200)*10
#     bill=first_100+second_100+remaining
# print(":---Total Bill---:")
# print("bill:",bill)


# gb=float(input("enter GB:"))
# if gb<=1:
#     bill=gb*0
# elif gb<=4:
#     first_1gb=gb*0
#     rem_gb=(gb-1)*15
#     bill=first_1gb+rem_gb
# else:
#     first_1gb=gb*0
#     next_4gb=gb*15
#     rem_gb=(gb-5)*25
#     bill=first_1gb+next_4gb+rem_gb
# print(":---Total Bill---:")
# print("bill:",bill)

#slab wise
# litres=int(input("enter the litres:"))
# if litres<=50:
#     print(litres*1)
# elif litres<=100:
#     print(litres*2)
# else:
#     print(litres*3)

# hours=int(input("enter  hours:"))
# if hours<=1:
#     print("30rs")
# elif hours<=3:
#     print("60rs")
# else:
#     print("90rs")

# month=int(input("enter duration of month:"))
# if month==1:
#     print("100rs")
# elif month==3:
#     print("250rs")
# else:
#     print("450rs")


# meal_type=input("enter meal type:(Breakfast/Lunch/Dinner)")
# if meal_type=='Breakfast':
#     print("30rs")
# elif meal_type=='Lunch':
#     print("50rs")
# else:
#     print("40rs")





tup=(1,2,3,'raj',7,8,9)
for t in tup:
    print(t)