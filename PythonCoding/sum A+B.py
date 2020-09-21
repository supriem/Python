# Write a program that asks the user for a number n and prints the sum of the numbers 1 to n

num = int(input("Enter value for n: "))

def sq(num):
    return lambda num: num*num

print(sq(num))
