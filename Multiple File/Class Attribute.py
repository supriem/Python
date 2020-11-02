# customize string representation of objects

class my_color():
    def __init__(self):
        self.red = 12
        self.green = 38
        self.blue = 78
        
        
    # TODO : use getattr to dynamically return value
    def __getattr__(self, attr):
        if attr == 'rgbcolor':
            return (self.red, self.green, self.blue)
        else:
            raise AttributeError
    
    # TODO : use setattr to dynamically return value
    def __setattr__(self, attr, val):
        super().__setattr__(attr, val)
        
    # TODO : to use dir to list available properties
    def __dir__(self):
        pass

def main():
    #create instance of color class
    cls1 = my_color()
    print(cls1.rgbcolor)
    
    # Print the value of computed attributte

if __name__ == "__main__":
    main()