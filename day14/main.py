
from art import logo,vs
from game_data import data
import random
#display art
print(logo)
score=0
def format_data(account_a):
    #format the account data into printable format
    """format the account data into printable format """
    account_name=account_a["name"]
    account_descr=account_a["description"]
    account_country=account_a["country"]
    print(f"{account_name}, a {account_descr}, from {account_country}")
def check_answer(guess,a_followers,b_follwers):
    """use if statement to check if user is correct"""
    if a_followers>b_follwers:
        return guess=="a"
    else:
        return guess=="b"

game_should_continue=True
while game_should_continue:
#generate a random accouny from the game data
    account_a=random.choice(data)
    account_b=random.choice(data)
    if account_a==account_b:
        account_b=random.choice(data)
    print(f"compare A:{format_data(account_a)}.")
    print(vs)
    print(f"compare B:{format_data(account_b)}.")
    #ask user for a guess
    guess=input("who has more followers?type 'A' or ''B':").lower()
    #check if user is correct

    ## get followe count of each accoount
    a_follower_count=account_a["follower_count"]
    b_follower_count=account_b["follower_count"]
    is_correct=check_answer(guess,a_follower_count,b_follower_count)

#give user feedback on their guess
#score keeping
    if is_correct:
        score+=1
        print(f"you're right! current score:{score}'")
    else:
        print(f"dorry, that's wrong. final score :{score}")
#make the game rapeatable
#making account at postion b become the next account at postion a
#clear the screen between rounds