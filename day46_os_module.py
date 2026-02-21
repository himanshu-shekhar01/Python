#automatically aap har folder ke andar 1file delete ya banaa sakte ho 
#ek baar me kai saari jagah banaa skte hai.
import os

# if (not os.path.exists("data")):
#     os.mkdir("data")

# for i in range(0,100):
#     os.mkdir(f"data/Day{i+1}") 

#it creates all folders name day1-100

#for rename file 
#os.rename("data/Day1","data/Day1_new")

# for i in range(0,100):
#     os.rename(f"data/Tutorial{i+1}", f"data/Tutorial {i+1}")

#for delete file
#os.rmdir("data/Day1_new")
#for delete folder
#os.rmdir("data")

folders = os.listdir("data")
print(folders)

for folder in folders:
    print(folder)
    print(os.listdir(f"data/{folder}"))

print(os.getcwd()) #to check you are where in directory

# you can also change directory
# print(os.getcwd)
# os.chdir("/users")
# print(os.getcwd)


#you have to read os module from online
