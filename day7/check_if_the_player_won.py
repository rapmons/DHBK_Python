import random


word_list=["a","b","c"]
chosen_word=random.choice(word_list)
print(f"psst, the solution is{chosen_word}")

word_length=len(chosen_word)
dispay=[]
word_length=len(chosen_word)
for _ in range(word_length):
    dispay+="_"
print(dispay)

end_of_game=False
while not end_of_game:
    guess=input("guess a letter:").lower()
    for position in range(word_length):
        letter=chosen_word(position)
        print(f"current position:{position}\n current letter:{letter}\n Guessed letter:{guess}")

        if letter==guess:
            dispay[position]==letter

    print(dispay)
    if"_" not in dispay:
        end_of_game=True
        print("you win")