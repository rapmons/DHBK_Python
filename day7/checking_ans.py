#picking a random words and checking answers
import random
word_list=["a",'b',"c"]
chosen_word=random.choice(word_list)
answer= input("guess a letter :").lower()
for letter in chosen_word:
    if answer== chosen_word:
        print("right")
    else :
        print("wrong")

