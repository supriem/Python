# WAP to swap numbers without using temporary variable

a = int(input("Enter A: "))
b = int(input("Enter B: "))



a = a+b
b = a - b
a = a-b 
print("Swpped values are", a,b)