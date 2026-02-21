#import in python is the process of loading code from a python module into the current namespace.
#importing a module is done by using the import keyword.
# import math
# print(math.pi)
# print(math.sqrt(16))

#agar ek function laane ka man kare toh
# from math import sqrt,pi
#this is good
# result = sqrt(9) * pi
# print(result) #3.0


# from math import *
#this is not a good practice because if you have 2 folder with same name then it will give error

# import math as m
# result = m.pi
# print(result)
# print(m.sin(90))

#dir function
#it is used for getting the list of all the attributes and methods of an object.

# print(dir(m))
# print(m.nan,type(m.nan)) #it is float

# from day45if__name__ import welcome,name
# welcome()
# print(name)

#aise aap ek file ko idhar import kar sakte hai

# import day45if__name__ as h
# h.welcome()
# print(h.name)

# import day45if__name__ as we

# we.welcome()
# bina __name__ ke do baar print ho rha tha ab ek baar hogaa


#idioms is a common pattern used in python script to determine whether the script is run directly or being imported as a module into another script

#aapke file ki band baj sakti hai jab aap file kahi aur se import karoge aur voh critical hua toh voh aapke computer ki file delete kar sakta hai