# Demo of usage of Nametuple

import collections

def main():
    # TODO: create a point namedtuple
    Point = collections.namedtuple("Point", "x,y")
    p1 = Point(10,20)
    p2 = Point(43,21)
    print(p1,p2)
    print(p1.x,p2.y)
    
    # TODO: use _replace to crete a new instance
    p1 = p1._replace(x = 1000)
    print(p1)
    
    
if __name__ == "__main__":
    main()