#function with inputs
#simple function
def greet():
    print("hello angela")
    print("how do you do angela")
    print("isn't the weather nice today?")
greet()

#function that allows for input

def greet_name(name):
    print(f"hello {name}")
    print(f"how do you do {name}")
    print("isn't the weather nice today?")
greet_name("angela")


#positional and keyword Arguments

def greet_with(name,location):
    print(f"Hello{name}")
    print(f"what is it like in {location}")

greet_with("nowhere","jack bauer")
# or greet_with(name="angela",location="London")

