#  give objects-number like behavior

class Point():
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __repr__(self):
        return "<Point x:{0}, y: {1} >".format(self.x, self.y)
    
    # implement addition
    
    def __add__(self, other):
        return Point(self.x + other.x, self.y + other.y)
    
    # implement subtraction
    def __sub__(self, other):
        return Point(self.x - other.x, self.y - other.y)
    # TODO: implement in-place addition
    def __iadd__(self,other):
       # return Point(self.x + other.x, self.y + other.y)
       
def main():
    # Declare some points
    p1 = Point(29,10)
    p2 = Point(24,45)
    print(p1,p2)
    print(p1 + p2) # we can't without defined __add__ method add  TypeError: unsupported operand type(s) for +: 'Point' and 'Point'
    # TODO: sutract two points
    p_sub = p2- p1
    print(p_sub)
    
    # TODO: perform in-place addition
        
if __name__ == "__main__":
    main()
    
    