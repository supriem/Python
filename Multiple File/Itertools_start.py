import itertools

def testFunction(x):
    return x < 40

def main():
    # TODO: cycle iterator can be used to cycle over a collection
    seq1 = ['ram','eur','sam','yur']
    cycle1 = itertools.cycle(seq1)
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1))
    print(next(cycle1)) # instead of thorwing it cycles list again
    
    # TODO: use counter to create a simple counter
    count1 = itertools.count(99,10)
    print(next(count1))
    print(next(count1))
    print(next(count1))
    print(next(count1))
    
    # TODO: accumulate creates an iterator that accumulates values
    vals = [10,20,30,39,50,40,10]
    print("\nWill give Cumulative Sum:")
    accum = itertools.accumulate(vals)
    print(next(accum))
    print(next(accum))
    print(next(accum))
    print("\n")
    ccum = itertools.accumulate(vals,max)
    print(next(ccum))
    print(next(ccum))
    print(next(ccum))
    print(next(ccum))
    print(next(ccum))
    print(next(ccum))
    
    
    
    # TODO: use chain to connect sequences together
    x = itertools.chain("ABCD","1234")
    print(list(x))
    
    # TODO: dropwhile and takewhile will return values untill condition to stop them is given
    print(list(itertools.dropwhile(testFunction, vals)))
    print(list(itertools.takewhile(testFunction, vals)))
    


if __name__ == "__main__":
    main()
     