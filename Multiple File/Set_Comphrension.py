# Demo of set comphrension

def main():
    # define a list of temperature data points
    ctemps = [0,12,34,100,36,29,49,40,40,40,40]
    f_lst = [(t*9/5) + 32 for t in ctemps]
    f_set = {(t*9/5) + 32 for t in ctemps} #use curly braces, no duplicates
    print("Lst_Com",f_lst)
    print("Set_Com",f_set)
    print(type(f_set))
    
    # TODO: build a set of unique Farh temp
    f_set = {(t*9/5) + 32 for t in ctemps if t >37}
    print("Conditioned f_set: ", f_set)
    # TODO: build a set from input source
    
    s_tmp = "A quick brown fox jump over the lazy dog"
    chars = {c.upper() for c in s_tmp if not c.isspace()}
    print("char without space: ",chars)
    
    # TO remove space
    
    print(chars)
 
 
 
 
if __name__ == "__main__":
    main()
