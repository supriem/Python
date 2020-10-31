# String contains unicode
# Bytes are raw 8-bit values

def main():
    # define some starting values
    b = bytes([0x41, 0x42,0x43, 0x44])
    print(b)
    
    s = "This is a string"
    print(s)
    
    # TODO: Try combining them print(s+b) will give an error
    s2 = b.decode('utf-8')
    print(s+ s2)
    # TODO encode 
    b2 = s.encode('utf-8')
    print(b+ b2)
    print(type(b+b2))
    
    # TODO : Try encoding with string to UTF-32
    b3 = s.encode('utf-32')
    print(b+b3)
    print(type(b+b3))

if __name__ == "__main__":
    main()