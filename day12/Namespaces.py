################### Scope ##################
enemies=1
def increase_enemies():
    enemies=2
    print(f"enemies inside fuction:{enemies}")
increase_enemies()
print(f"enemies outside fuction:{enemies}")

#local Scope
def drink_potion():
    potion_strength=2
    print(potion_strength)

drink_potion()
#print(potion_strength) err

#global scope
play_health=10
def game():
    def drink_potion():
     potion_strength=2
     print(play_health)
    drink_potion()
game()