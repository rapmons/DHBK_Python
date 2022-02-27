#control flow with if else and conditional operators
print("Welcome to the rollercoaster!")
height=int(input("what is your height in cm?"))
if height>120:
    print("you can ride the rollercoaster!")
else:
    print("sorry, you have to grow taller before you can ride")

#odd or even exercise
number=int(input("which number do you want to check?"))
if number%2==0:
    print("this is a even number.")
else:
    print("this is an odd number")

#nested if statements and dlif statements
print("Welcome to the rollercoaster!")
height=int(input("what is your height in cm?"))
if height>120:
    print("you can ride the rollercoaster!")
    age=int(input("what is your age?"))
    if age<12:
        print("please pay $5")
    elif age<=18:
        print("please pay $7")
    else:
        print("please pay $12")

else:
    print("sorry, you have to grow taller before you can ride")

#BMI 2.0
height=float(input("enter your height in m:"))
weight=float(input("enter your weight in kg"))
bmi=round(weight/height**2,2)
if bmi<18.5:
    print(f"your bmi is{bmi}, you are underwieght")
elif bmi<25:
    print(f"your bmi is {bmi},you have a nomal weinght")
elif bmi<30:
    print(f"your bmi is{bmi},you are overweight")
elif bmi<35:
    print(f"your bmi is {bmi}, you are obese")
else:
    print(f"your bmi is {bmi}, you are clinically obese")

# multiple if statements in succesion
bill=0
wants_photo=input("do you want a photo taken? Y or N")
if wants_photo=="Y":
    bill=bill+3

print(f"your final bill is{bill}")

#pizza order practice

print("welcome to pythonn Pizza Delveries")
size=input("what size pizza do you want ? S,M,or L")
add_pepperoni=input("do you want pepperoni? Y or N")
extra_cheese=input("do you want extra cheese? Y or N")
bill=0
if size=="S":
    bill+=15
elif size=="M":
    bill+=20
else:
    bill+=25
if add_pepperoni=="Y":
    if size=="S":
        bill+=2
    else:
        bill+=3
if extra_cheese =="Y":
    bill+=1
print(f"your final bill is ${bill}")

#logical Operator
bill=0
age= int(input("what is your age?"))
if age< 12:
    bill+=5
if age>=12 and age<45:
    bill+=10
else:
    bill+=11
print(f"your final bill is ${bill}")

#Love calculator Exercise
print("welcome to the Love calculator!")
name1=input("what is your name?\n")
name2= input("what is their name?\n")

combined_string = name1+name2
lower_case_string= combined_string.lower()
t=lower_case_string.count("t")
r=lower_case_string.count("r")
u=lower_case_string.count("u")
e=lower_case_string.count("e")

true= t+r+u+e
l=lower_case_string.count("l")
o=lower_case_string.count("o")
v=lower_case_string.count("v")

love= l+o+v+e
love_score=str(true)+str(love)

if int(love_score)<10 or int(love_score)>90:
    print(f"your love score is {love_score},you....")
elif int(love_score)>=40 or int(love_score)<=50:
    print(f"your love score is {love_score},you....")
else:
    print(f"your score is {love_score}")

#project Treasure Islan

