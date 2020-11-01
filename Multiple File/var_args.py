# Demonstrate the use of variable argument list

# TODO:  define a function  that takes variable arguments
def addition(*args):
    res = 0
    for arg in args:
        res += arg
    return res
def main():
    # TODO: pass different arguments
    print(addition(3,5,7,30))
    print(addition(65,34,34,7,8))
    
    # TODO: pass an existing list
    my_values = [1,3,56,3,7,2]
    print("Print sum from list: ",addition(*my_values))
    
    
if __name__ == "__main__":
    main()