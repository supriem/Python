# Read as 'deck' Double ended queue
import collections
import string

def main():
    # TODO: initialize deck with lowercase letter
    d = collections.deque(string.ascii_lowercase)
    #TODO: deque support the len() function
    print("item count: ", str(len(d)))
    
    # deques can be iterated over
    for ele in d :
        print(ele.upper(), end = ",")
    # TODO: manipulate items from either end
    d.pop()
    d.popleft()
    d.append(23)
    d.append(1)
    print("\n\n",d)
    #TODO: rotate the deque
    d.rotate(10)
    print("After 10 ele : ", d)
    

if __name__ == "__main__":
    main()