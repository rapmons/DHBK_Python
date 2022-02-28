import random


word_list=["a","b","c"]
chosen_word=random.choice(word_list)
print(f"psst, the solution is{chosen_word}")

dispay=[]
word_length=len(chosen_word)
for _ in range(word_length):
    dispay+="_"
print(dispay)

guess=input("guess a letter:").lower()
for position in range(word_length):
    letter=chosen_word(position)
    if letter==guess:
        dispay[position]==letter

print(dispay)