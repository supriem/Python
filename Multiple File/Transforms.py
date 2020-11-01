# use transform functions like sorted, fileter, map

def filterFunc(x):
    if x%2 == 0:
        return False
    return True
def filterFuncLower(x):
    if x.islower() == True:
        return True
    else:
        return False
def sq_func(x):
    return x**2
    
def toGrade(x):
    if x>90:
        return "A"
    elif x>80:
        return "B"
    elif x>70:
        return "c"
    else:
        return "WORKWORKWORKWORK"
    


def main():
    nums = [1,3,5,6,3,5,76,3,7,54,67,9]
    chars = "dsjfmdksjdnviSshjxzHHJHDa=ebra"
    grades = (81,45,79,58,70,38,84)
    
    # TODO: Use filter to remove items from list
    odds = list(filter(filterFunc, nums))
    print(odds)
    
    # TODO: use filter on non-numeric sequence of values
    lowers = list(filter(filterFuncLower, chars))
    print(lowers)
    
    # TODO: use map to create new sequence of values
    squared_nums = list(map(sq_func,nums))
    print(squared_nums)
    
    # TODO: use sorted and map to change numbers to grades
    grades = sorted(grades)
    letters_grades = list(map(toGrade, grades))
    print(letters_grades)

if __name__ == "__main__":
    main()
    