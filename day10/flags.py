#calculator
from art import logo
print(logo)
#add
def add(n1,n2):
    return n1+n2
#subtract
def subtract(n1,n2):
    return n1-n2
#multiply
def multiply(n1,n2):
    return n1*n2
#divide
def divide(n1,n2):
    return n1/n2


operations={
    "+":add,
    "-":subtract,
    "*":multiply,
    "/":divide
}
def calculator():
    num1= int(input("what's the number ?:"))
    num2=int(input("what's the next number?"))
    for symbol in operations:
            print(symbol)
    should=True
    while should:
        operation_symbol=input("pick an operation form the line above:")
        calculation_function=operations[operation_symbol]
        answer=calculation_function(num1,num2)

        print(f"{num1} {operation_symbol} {num2}={answer}")

        if input(f"type 'y' to continue calculating with {answer}:"=="y"):
            num1=answer
        else:
            should= False


