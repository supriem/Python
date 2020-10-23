from collections import namedtuple

Student = namedtuple('Student', ['name', 'age', 'roll'])


# Adding Values

S = Student('ram',28,'23')

print(S)
print(S.roll)
print(S[0])
print(S[-1])