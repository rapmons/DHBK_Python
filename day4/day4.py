#Randomisation
#Random module
import random
from turtle import position
from xml.sax import handler
ramdom_integer=random.randint(1,10)
print(ramdom_integer)

#module
import my_module
print(my_module.pi)

random_float=random.random()
print(random_float)
# create random number between 0 and 5
random_float*5
love_score= random.randint(1,100)
print(f" your love score is {love_score}") 

#Random Exercise
test_seed=int(input("create a seed number:"))
random.seed(test_seed)
random_side=random.randint(0,1)
if random_side==1:
    print("Heads")
else:
    print("Tails")


#lists
states_of_america=["delaware","pennsylvania","sshhs"]
print(states_of_america[1]) #pennsylvania
print(states_of_america[-1]) #phan tu cuoi cung



# who will pay the bill

test_seed=int(input("create a seed number:"))
random.seed(test_seed)
nameAsCSV= input("give me everybody's names,seperated by a comma")
names=nameAsCSV.split(",")
num_items=len(names)
random_choice=random.randint(0,num_items-1)
print(names[random_choice]+"is going to buy the meel today")

#nested Lists
fruits=["a","b","c"]
vegetables=["1","2","3"]
dirty_dozen=[fruits,vegetables]
print(dirty_dozen)

#treasure Map
row1=[" "," "," "]
row2=[" "," "," "]
row3=[" "," "," "]
map=[row1,row2,row3]
print(f"{row1}\n{row2}\n{row3}")
position= input("where do you want to put the treasure?")

horizonal=int(position[0])
vertical=int(position[1])
map[vertical-1][horizonal-1]="x"
print(f"{row1}\n{row2}\n{row3}")


