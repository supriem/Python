# customize string representiation of objects

class Person():
    def __init__(self):
        self.fname = "Suprim"
        self.lname = "Regmi"
        self.age = 29
        
    # TODO: use __repr__ to create a string useful for debugging
    def __repr__(self):
        return "<Person class fname:{0}, lname:{1}, age: {2} >".format(self.fname,self.lname, self.age)
    
def main():
    # create a new person object
    cls1 = Person()
    
    # Use different python function to convert it to string
    print(repr(cls1))
    print(str(cls1))
    print("Formated {0}".format(cls1))

if __name__ == "__main__":
    main()