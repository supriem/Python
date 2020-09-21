def obtain_data_from_bensound():
    return """
    this is some dummy song file
    written in text format
    
    """


def save_to_disk(data, filename, directory = ".", extension = "txt"):
    #handler = open(filename, "w")
    #handler.write(data)
    #handler.close()
    with open(filename + extension, "w") as handler:
        handler.write(data)

data = obtain_data_from_bensound()
save_to_disk(data = content, filename = "dummy.txt")

