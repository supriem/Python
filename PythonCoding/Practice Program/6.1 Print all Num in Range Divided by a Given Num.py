
low = int(input("Enter lower range : "))
high = int(input("Enter higher bound : "))

enter_num = int(input("Enter a number: "))

divisor_lst = []
for i in range(low, high):
    if i % enter_num ==0:
        divisor_lst.append(i)
        
print(divisor_lst)
    