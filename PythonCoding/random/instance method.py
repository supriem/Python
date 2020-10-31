# demonstrate instance method

class Student:
    
    #creating static class var #above init
    school = 'TU' 
    def __init__(self,m1,m2,m3):
        self.m1 = m1
        self.m2=  m2
        self.m3 = m3
    
    def avg(self):  # When we are passing self it means it belongs to some obj
        return (self.m1+ self.m2+ self.m3)/3
    """THE avg is instance method because it works with object"""
        
        
s1 = Student(23,45,22) #1st object
s2 = Student(89,49,50)

print(s1.avg())
print(s2.avg())