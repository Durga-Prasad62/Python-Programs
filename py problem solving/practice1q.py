# Take a number from user.

# If it's > 0 → "Positive"

# If it's < 0 → "Negative"

# If it's 0 → "Zero"""
num=int(input("enter a number"))
if num==0:
    print("zero")
elif num>0:
    print("positive")
else:
    print("negative")


#  2. Check Leap Year
# Ask the user for a year.
# A year is a leap year if:

# Divisible by 4 and not divisible by 100
# or

# Divisible by 400


year=int(input("enter a year"))
if (year%4==0 and year%100!=0) or year%400==0:
    print("leap year")
else:
    print("not a leap year")



# 3. Vowel or Consonant
# Input: a single letter

# If it's in a, e, i, o, u → Vowel

# Else if it’s a letter → Consonant

# Else → Invalid input (like number or symbol)

user=(input("enter a character:+"))
if ('A'<=user <='Z') or ('a'<=user <= 'z'):
    if user in "aAEeIiOoUu":
     print("vowel")
    else:
      print("consonent")
else:
  print("invalid input")


# 🔥 Logic Challenge Set – Level 2 (Medium)
# 🔸 4. Greatest of Three Numbers
# Take three numbers as input.
# Print the largest one.

# Try using:

# Simple if-elif-else

# Then try using nested ifs

num1=float(input("enter number1:"))
num2=float(input("enter number2:"))
num3=float(input("enter number3"))
if num1>num2 and num1>num3:
    print(num1,"is greater")
elif num2>num3 and num2>num1:
    print(num2,"is greater")
else:
    print(num3,"is greater")


num1=float(input("enter number1:"))
num2=float(input("enter number2:"))
num3=float(input("enter number3"))
if num1>num2 and num1>num3:
    print(num1,"is greater")
else:
    if num2>num1 and num2>num3:
        print(num2, "is greater")
    else:
        print(num3,"is greater")


# 🔸 5. Triangle Type Based on Sides
# Take 3 sides as input:

# If all 3 sides are equal → Equilateral

# If 2 sides are equal → Isosceles

# If all are different → Scalene

# If triangle is not valid (sum of 2 sides ≤ 3rd), print "Invalid"""



side_1=int(input("enter the side1:"))
side_2=int(input("enter the side2:"))
side_3=int(input("enter the side3:"))

if (side_1 + side_2 <= side_3) or (side_2 + side_3 <= side_1) or (side_1 + side_3 <= side_2):
    print("Invalid Triangle")
elif side_1==side_2==side_3:
    print("Equilateral")
elif (side_1 == side_2) and (side_2 != side_3) and (side_1 != side_3):
    print("Isosceles")
elif(side_1 != side_2) and (side_2 != side_3) and (side_1 != side_3):
    print("Scalene")

   
# """🔸 6. Grade with Validation
# Ask marks (0 to 100).
# If marks > 100 or < 0 → Invalid
# Else:

# ≥ 90 → A

# 75–89 → B

# 60–74 → C

# 40–59 → D

# Below 40 → Fail"""

marks=int(input("enter the marks"))
if marks>=90:
    print("Grade A")
elif marks>=75:
    print("Grade B")
elif marks>=60:
    print("Grade:C")
elif marks>=40:
    print("Grade:D")
else:
    print("Fail")