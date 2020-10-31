# use iterator functions like enumerate, zip, iter, nextabs

def main():
    # define a list of days in Engish and Nepali
    days = ["sun", "mon", "tue", "wed", "thu", "fri", "sat"]
    daysN = ["ait","som","man","bud","bhi","suk","san"]
    
    
    # Use iter to create an iterator over collection
    i = iter(days)
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    print(next(i))
    #print(next(i)) # Stop Iteration
    
    # iterate using function and sentinel
    with open("textfile.txt","r") as fp:
        for line in iter(fp.readline, ""):
            print(line)
    # use  regular iteration over days
    for m in days:
        print(m)
        
    for m in range(len(days)):
        print(m+1, days[m])
        
    # using enumerate reduces code and provides counter
    for i,m in enumerate(days, start = 1):
        print(i,m)
    print("\n")
    #use zip to combine sequences
    a = zip(days,daysN)
    print(list(a))
    print("\n\n")
    for m in zip(days,daysN):
        print(m)
        
    # Enumerate and zip
    for m in enumerate(zip(days,daysN), start = 1):
        print(m)
    
if __name__ == "__main__":
    main()