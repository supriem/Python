from collections import Counter

def main():
    # lst student in class 1
    class1 = ["Ram","Ram", "Yurika", "Gita","Hari","Shyam","Chame","ram","RAMA","Ram"]
    #lst of students in class2
    class2 = ["Billy", "Jonas", "Martha","Mikkel", "7","Susan"]
    
    # TODO: create a counter for class2 and class2
    c1 = Counter(class1)
    c2 = Counter(class2)
    # How many student in class1 named ram
    print("Count Ram: ", c1["Ram"])
    
    # How manny students are in class1
    print(sum(c1.values()), "Students in class 1")
    
    # Combine two classses
    c1.update(class2)
    print(sum(c1.values()))
    
    # Most common name in 2 class
    print(c1.most_common(3))
    

if __name__ == "__main__":
    main()