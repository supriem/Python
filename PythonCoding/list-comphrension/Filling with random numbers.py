from random import randint

low = int(input("Enter a number min : "))
high = int(input("Enter a number max: " ))

a = [randint(low,high) for i in range(10)]

print(a)