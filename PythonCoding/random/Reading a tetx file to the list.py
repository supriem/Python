data = []

for i in open('text_file.txt'):
    data.append(i)

    #if data[i][-1] == '\n':
        #data[i] = data[i].strip()
     #   data[i] = data[i][:-1]
        
with open("text_file.txt", "r") as f:
    lines = f.readlines()
    print(lines)

#print(data)