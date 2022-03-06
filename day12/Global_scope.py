from random import randint
from art import logo
print(logo)

EASY_LEVEL_TURNS=10
HARD_LEVEL_TURNS=5
def check_answer(guess,answer,turns):
    if guess>answer:
        print("too high.")
        return turns -1
    elif guess <answer:
        print("too low.")
        return turns-1
    else:
        print("you got it! the answer was {answer}")


def set_difficult():
    level=input("choose a difficulty , Type 'easy' or 'hard':")
    if level=="easy":
        return EASY_LEVEL_TURNS
    else:
        return HARD_LEVEL_TURNS

def game():
    print("welcome to the Number Guessing Game!")
    print("I'm thingking of a number between 1 and 100")
    answer=randint(1,100)
    print(f"psst,the correct answer is {answer}")

    turns=set_difficult()
    
    guess=0
    while guess!=answer:
        print(f"you have {turns} attempts renaining to guess the number.")
        guess= int(input("make a guess:"))
        turns=check_answer(guess,answer,turns)
        if turns==0:
            print("you've run out of guesses,you lose.")
            return
game()