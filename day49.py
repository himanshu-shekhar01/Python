# yahaa aapko pataa lageaga ek file ko kaise read kiya jaata hai kase usme write karte hai , or file binary ho toh kaise read write karenge aao dekhte hai ..
# f = open("day42.py","r")  
# and default is r mode  # f = open("day42.py") you can use also like this

# error ayegaa because in that time it is not exist, 
#if exists then it output comes

# f = open("poem.txt","r")
# f = open("poem.txt","w") # if youu write this istead of r then cant read
# # print(f)  #it prints some object if we want to read 
# text  = f.read()
# print(text)
# f.close()


# If the file is located in a different location, you will have to specify the file path, like this:
# f = open("/Users/himanshu/Documents/python/day42.py", "r")
# print(f.read())
# f.closed() #if same then ok

# if you give inside read(5), then come 5 characters

# You can return one line by using the readline() method:

# you give b mode for image , pdf, and other type file.

# with open("file.txt","w") as f:
#     f.write(" oops i will delete previous content") #it is automatic closed

# To delete a file, you must import the OS module, and run its os.remove() function:
# import os
# os.remove("file.txt")

# import os
# if os.path.exists("demofile.txt"):
#   os.remove("demofile.txt")
# else:
#   print("The file does not exist")

# To avoid getting an error, you might want to check if the file exists before you try to delete it:
# To delete an entire folder, use the os.rmdir() method:  You can only remove empty folders.




