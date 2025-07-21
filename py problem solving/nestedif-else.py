# marks=int(input("enter a number:"))
# if marks>=90:
#     print("Grade:A")
# else:
#     if marks>=75:
#         print("Grade:B")
#     else:
#         if marks>=60:
#             print("Grade:C")
#         else:
#             if marks>=40:
#                 print("Grade:D")
#             else:
#                 print("Fail")



# Ask the user for their age.

# If age is 18 or above, print "Eligible to vote",

# If age is between 18 and 60, print "Adult voter"

# If age is above 60, print "Senior voter"

# Else, print "Not eligible to vote".



# age=int(input("enter your age:"))
# if age>=18:
#     print("Eligible to vote")
#     if age>=18 and age<=60:      #age>=18 should  remove  you already know age ≥ 18, for optimal code
#         print("Adult voter")
#     else:
#         if age>60:
#             print("Senior Voter")
# else:
#   print("Not Eligible to vote")



# Take three angles as input and:

# If their sum is 180, it's a valid triangle.

# If all angles are equal → print "Equilateral"

# If two are equal → print "Isosceles"

# Else → print "Scalene"

# Else → print "Invalid triangle"

# angle_1=int(input("enter the  first angle:"))
# angle_2=int(input("enter the  second angle:"))
# angle_3=int(input("enter the third angle:"))
# sum=angle_1+angle_2+angle_3
# if sum==180:
#    print("its a valid triangle")
#    if angle_1==angle_2==angle_3:
#      print("Equilateral")
#    else:
#       if angle_1==angle_2!=angle_3:
#         print("Isosceles")
#       else:
#        print("Scalene")
# else:
#     print("Invalid Traingle")




# Ask the user to enter the color of the traffic light (red, yellow, green):

# If red:

# Ask if the road is empty (yes/no)

# If yes → print "Wait anyway"

# If no → print "Definitely stop"

# If yellow → print "Get ready"

# If green → print "Go"

# color=(input("enter the color of the traffic light:"))
# if color=="red":
#     road=input("enter the road is empty  (yes/no)")
#     if road=='yes':
#         print("wait any way")
#     # else:
#     if road =='no':
#             print("Definitely stop")
# else:
#    if color=='yellow':
#         print("Get ready")
#    else:
#         if color=='green':
#             print("Go")



# Ask the user to enter a year.

# If divisible by 4:

# If divisible by 100:

# If divisible by 400 → Leap year

# Else → Not a leap year

# Else → Leap year

# Else → Not a leap year

# Also print if it’s a century year (divisible by 100)


year=int(input("enter a year"))
if year%4==0:
    if year%100==0:
        if year%400==0:
            print("leap year")
        else:
            print("not a leap year")
    else:
        print("leap year")
else:
    print("not a leap year")

if year%100==0:
    print("century year")









     

        




