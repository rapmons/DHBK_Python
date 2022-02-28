#Using the for loop in python lists
from numpy import average


fruits=["apple","peach","pear"]
for fruit in fruits:
    print(fruit)
    print(fruit+"pie")
print(fruits)

#average height

student_heights=input("input a list of student heights").split()
for n in range(0,len(student_heights)):
    student_heights[n]=int(student_heights[n])
print(student_heights)
total_height=0
for height in student_heights:
    total_height+= height
print(total_height)

number_of_students=0
for student in student_heights:
    number_of_students+=1
average_height=round(total_height/number_of_students)
print(average_height)

#high score 

student_score=input("input a list of student score")
for n in range(0,len(student_score)):
    student_score[n]=int(student_score[n])
print(student_score)
highest_score=0
for score in student_score:
    if score>highest_score:
        highest_score=score

print(f"the highest score in the class is:{highest_score}")


#for loop
for number in range(1,10):
    print(number) # 1->9

#add evens numbers

total=0
for number in range(2,101,2):
    total+=number
print(total)

total2=0
for number in range(1,101):
    if number %2==0:
        total2+=number

print(total2)


# interview question
for number in range(1,101):
    if number%3==0 and number % 5:
        print("fizzBuzz")
    elif number %3 ==0:
        print("fizz")
    elif number %5==0:
        print("buzz")
    else:
        print(number)
    
# project create password
import random

letters=[]
numbers=[]
symbol=[]
print("welcome to the Pypassword generator!")
nr_letters=int(input("how many letters would you like in your password?\n"))
nr_symbols=int(input(f"how many symbols would you like?\n"))
nr_number=int(input(f"how many number eould you like?\n"))
password=[]

for char in range(1,nr_letters+1):
    password.append(random.choice(letters))
for char in range(1,nr_symbols+1):
    password.append(random.choice(symbol))
for char in range(1,nr_number):
    password.append(random.choice(numbers))

random.shuffle(password) # thay doi thu tu
print(password)