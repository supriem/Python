""" Count vowels in given sentence"""

# get sentence
# loop through each character
# if vowels increment counter

counter = 0
sentence = input("Please  enter  a sentence: ")

for char in sentence.lower():
    if char in ("a","e","i","o","u"):
        counter+=1
print(counter)