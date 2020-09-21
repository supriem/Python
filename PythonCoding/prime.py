""" generate list of first 50 prime numbers"""
num = int(input("Enter number: "))
op = num-1
is_prime = True

while op>1:
    if num % op == 0:
        is_prime = False
    op -=1

if is_prime:
    print("number: {} is prime".format(num))

selse:
    print("number: {} is not a prime".format(num))
    