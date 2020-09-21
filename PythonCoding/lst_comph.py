"""numbers = []
for i in range(1, 30):
    numbers.append(i)
    
    """

# using list comphrension
numbers2 = [i for i in range(1,30)]
print(numbers2)


num3 = [i for i in range (1,30) if i%3 ==0 ]
print(num3)