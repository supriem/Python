#************* Method 1 ******************************
"""lst = [2,2,2,2,10]
sum = 0
for i in range(0, len(lst)):
    sum = sum+lst[i]
print(sum)
avg = sum/(len(lst))
print("The average of above list is {}".format(avg))
"""
#************** Method 2 *******************************
num = int(input("enter the numbers of elements you want in list: "))
num_lst = []
for i in range(0,num):  # or 1-5
    ele = int(input("Enter value: "))
    num_lst.append(ele)

print(num_lst)

avg = sum(num_lst)/len(num_lst)
print("The avg of the list you have entered is {}".format(avg))
    