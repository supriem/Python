class Student:
    
    #creating static class var 
    school = 'TU'  # class variable
    def __init__(self,m1,m2,m3):
        self.m1 = m1 # instance variable can be used with instance method
        self.m2=  m2
        self.m3 = m3
    
    # instance method
    def avg(self):  # When we are passing self it means it belongs to some obj
        return (self.m1+ self.m2+ self.m3)/3
    # we can.not use student.avg but have to s1.avg
    # tyepes in instance -> accessor(just fetch value) -> mutator(modify)
    @classmethod
    def info(self):
        return cls.school
    
   
        


s1 = Student(23,45,22)
s2 = Student(89,49,50)
# fetch value
print(s1.m1)
"""   def get_m1(self.m1):
                        return self.m1
        Instead we def funvtion
        """
print(s1.avg())
print(s2.avg())


# we can access class var by
print(Student.info())
