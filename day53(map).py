# def double(n):
#     return n*2

# numbers = (1,2,3,4,5)
# result = map(double,numbers)
# print(list(result))

# def cube(x):
#     return x * x * x

# aap cube function naa bnaake direct lambda bnaa sakte ho
# cube replace of lambda x: x * x * x

# l = [2,3,4,8,9]
# newl = []

# for i in l:
#     newl.append(cube(i))
# print(newl)

# this is very bekaar way to making a new cube list using old list.
#better option is use karo map
# map function is used to take input a sequence of element and return a sequence of elements.

# newl = map(cube,l)
# print(list(newl))

#cube jo hai lambda function bhi ho skataa hai..

#filter function

#jaisa naam viasa kaam 
# l = [2,3,4,8,9]

# def filter_function(x):
#     return x>4

# newnewl = filter(filter_function,l)
# print(list(newnewl))


# reduce function ko import karnaa padtaa hai.
from functools import reduce
l = [1,2,3,4,5]
result = reduce(lambda x,y : x+y, l)

print(result)



