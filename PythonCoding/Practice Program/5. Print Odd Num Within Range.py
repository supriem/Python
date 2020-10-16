# WAP to print odd number within given range

from_ = int(input(" Enter lower  number: "))
to = int(input("Enter higher num: "))
odd_lst = []
for n in range(from_, to+1):
    if n%2 != 0:
        odd_lst.append(n)
    else:
        print("Number is Even", n)
        
print("odd nums are", odd_lst)