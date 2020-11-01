# Demo of how to use list comphrension

def main():
    # define two lists of numbers
    odds = [1,5,7,9,3,7,9]
    evens = [2,4,6,8,20]
    
    # TODO: perform a mapping and filter function on a list
    evenSquared = list(map(lambda e: e**2,evens))
    print(evenSquared)
        # sq to num greater than4 less than 14
    CustomSq = list(map(lambda e: e**2,filter(lambda e: e>4 and e<16,evens)))
    print(CustomSq)
    
    # TODO: derive a new lst of num frm new lst
    evenSquared = [e**2 for e in evens]
    print("Printing Even Squared: ",evenSquared)
    # TODO: Limit the items operated on weith a predicate condition
    
    oddSquared = [e**3 for e in odds if e > 3 and e < 16 ]
    print(oddSquared)
    

if __name__ == "__main__":
    main()