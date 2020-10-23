# get word in reverse order
sentence = "A quick brown fox"
print(sentence[::-1])
# o/p:  xof nworb kciuq A

# using aplit
slist = sentence.split(" ")

print(slist)
# o/p : ['A', 'quick', 'brown', 'fox']

print(slist[::-1])

# Method 2

revlist = reversed(slist)
print(revlist)
print(list(revlist))

