# Keyword Only Args

# Use keyword only arguments  help ensure code clarity

def my_func(arg1, arg2, *, supressException = False):
    pass

def main():
    # try to call function without keyword
    my_func(1,2,supressException = True)
    # The function takes only 2 args to pass 3 we have to explictly define last keyword(suprssException)



if __name__ == "__main__":
    main()