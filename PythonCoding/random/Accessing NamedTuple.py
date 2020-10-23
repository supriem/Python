from collections import namedtuple

#Declaring
Student = namedtuple('Student', ['name','age', 'program'])

# Adding Values
S = Student('josh',24, 'stat')

# Accession Values
print(S[0])
print(S.age)
print(getattr(S, 'program'))


# replacing values
print("Modified Namedtuple is")
print(S._replace(age = 29))
