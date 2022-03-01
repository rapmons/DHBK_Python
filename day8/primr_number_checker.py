from numpy import number


def prime_cheker(number):
    for i in range(2,number):
        if number % i ==0:
            is_prime=False
    if is_prime:
        print("is's a prime number.")
    else:
        print("it's not a prime number.")
    


n= int(input("check this number:"))
prime_cheker(number=n)
