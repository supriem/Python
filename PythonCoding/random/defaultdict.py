from collections import defaultdict

def default_value():
    return "Not Present"
my_dict = defaultdict(default_value)

my_dict["ele1"] = 1
my_dict["ele2"] = 2

print(my_dict["ele1"])
print(my_dict["ele2"])
print(my_dict["ele3"])