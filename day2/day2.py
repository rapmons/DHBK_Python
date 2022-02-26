# Data types
#String
print("Hello"[0])
#->H
print("123"+"345")
#integer
print(123+345)
#float
print(3.14159)
#boolean
True
False

#type conversion
num_char=len(input("what is your name?"))
print("your name has"+str(num_char)+" characters.")
print(type(num_char)) # int
a=float(123)
print(type(a)) #float
print(70+float("100.5")) #170.5

#data types
two_digit_number=input("type a two digit number")
print(type(two_digit_number))
print(int(two_digit_number[0])+int(two_digit_number[1]))


#Operations
a=float(123)
print(type(a))
print(str(70)+str(100))

#PEMDASLR
# ()
# **
# * /
# +-
print(3*3+3/3-3) #7.0
print(3*(3+3)/3-3) #3.0


#BMI Calculator Exercise
height=int(input("enter your height in m:"))
weight=int(input("enter your weight in kg:"))
res= weight/(height**2)
print("BMI="+str(res))


#number manipulation and F string
print(int(8/3)) # 2
print(round(8/3,2))#2.67
print(8//3)#2
score=0
print("your score is"+str(score))
print(f"your score is{score}") # your score is 0

#your life in weeks

age=int(input("what is your current age"))

years_remaining=90-age
day= years_remaining*365
weeks=years_remaining*52
month=years_remaining*12
print(f"you have {day} day,{weeks} weeks,and {month} months left");

#project Tip

print("welcome to the tip calcutor!")
bill=float(input("what was the total bill?$"))
tip=int(input("how much tip would you like to give? 10,12,or 15?"))
people= int(input("How many people to split the bill"))
tip_as_percent=tip/100
total_tip_amount=bill*tip_as_percent
total_bill=bill+total_tip_amount
bill_per_person=total_bill/people
final_amount=round(bill_per_person,2)
print(f"Eac person should pay:${final_amount}")
