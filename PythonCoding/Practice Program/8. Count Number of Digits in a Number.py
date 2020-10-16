# WAP to count number of digits in given integer

to_be_counted = int(input("Enter a number which digit is going to be counted : "))
count = 0
while(to_be_counted > 0):
    to_be_counted //= 10 
    count+=1
    print("count number:", count)
  
print("The num of digits = ", count)
    
