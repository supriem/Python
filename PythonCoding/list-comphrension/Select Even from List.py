low = int(input("Enter a number min : "))
high = int(input("Enter a number max: " ))

lst = []

for i in range(low,high+1):
    lst.append(i)

print(lst)
even_lst = [ele for ele in lst if  ele% 2 ==0]

print("Even List is ",even_lst)