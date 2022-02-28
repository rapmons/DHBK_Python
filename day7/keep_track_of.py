import random


word_list=["a","b","c"]
chosen_word=random.choice(word_list)
word_length=len(chosen_word)
lives=6
print(f"psst, the solution is{chosen_word}")
dispay=[]
for _ in range(word_length):
    dispay+="_"

end_of_game=False
while not end_of_game:
    guess=input("guess a letter:").lower()
    for position in range(word_length):
        letter=chosen_word[position]
        if letter==guess:
            dispay[position]==letter
        else:
            print("no match")

    if guess not in chosen_word:
        lives-=1
        if lives==0:
            end_of_game=True

    print(f"{''.join(dispay)}")      
    if "_" not in dispay:
        end_of_game=True
        print("you win") 
