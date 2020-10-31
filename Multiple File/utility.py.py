# demonstrate built-in utility function

def main():
    lst1 = [1,2,3,4,5,0,9,10]
    
    # ANY: will return true if any of the sequence is true
    print(any(lst1)) # Will return true except 0 all are in sequence
    # ALL : will return True iff all valeus are True # Since 0 is not true
    print(all(lst1))
    # MIN & MAX :
    print("min: ", min(lst1), "max: ",max(lst1))
    # SUM
    print("Sum :" ,sum(lst1))

if __name__ == "__main__":
    main()