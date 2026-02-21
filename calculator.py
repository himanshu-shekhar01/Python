print("What is your name?")
name = input()
print("Hello, "+ name)

a = int(input("Enter your num1: "))
b = int(input("Enter your num2: "))

opr = input("type operator: ")

if(opr=="+"):
    print(a+b)
elif(opr=="-"):
    print(a-b)
elif(opr=="*"):
    print(a*b)
elif(opr=="/"):
    print(a/b)
elif(opr=="%"):
    print(a%b)
    