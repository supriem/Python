# print foo if given num is multiple of 3
# print bar if given num is multiple of 5
# print FooBar is both divisible by 3 & 5

n =  int(input("Enter a number: "))

if n/3 == 0 and n/5 == 0:
    print("FooBar")