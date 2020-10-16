enter_num = int(input("Enter a number : "))

for i in range(2, enter_num):
    if enter_num % i == 0:
        print("{A} is smallest integer divisor".format(A = i))
        break
    else:
        print("Number is Prime")
        break