# Use lambda as inplace functions

def CelsiusToFarenheit(tmp):
    return (tmp * 9/5) + 32

def FarhToCel(tmp):
    return (tmp-32)*5/9

def main():
    ctemps = [0,12,34,100,36,29,49,40,40,40,40]
    ftemps = [32,65,100,212]
    
    # TODO: use regular function to conver temp
    c_to_f = list(map(CelsiusToFarenheit, ctemps))
    print(c_to_f)
    f_to_c = list(map(FarhToCel, ftemps))
    print(f_to_c)
    
    # TODO : use lambda
    
    print("C_TO_F: ", list(map(lambda t:(t * 9/5) + 32 , ctemps)))
    print("F_TO_C: ", list(map(lambda t:(t-32)*5/9 , ftemps)))
        
    
    
    
if __name__ == "__main__":
    main()