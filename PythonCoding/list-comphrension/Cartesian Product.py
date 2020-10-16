# [f(x) for x in nums]
# [f(x) for x in nums if g(x)]

A = [1,3,5,6,7]
B = [2,4,6,7,8]

cartesian_product = [(a,b) for a in A for b in B]

print(cartesian_product)