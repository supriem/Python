lst = []
res = []

low = int(input("Enter lower range : "))
high = int(input("Enter higher bound : "))


#for i in range(low,  high+1):
#    lst.append(i)
        

n = int(input("Enter a number ..: "))

y = int(high/n)

for i in range(low, high+1):
    for j in range(1,y+1):
        if n *j== i:
            res.append(i)
            
print(res)
    
        

    
        