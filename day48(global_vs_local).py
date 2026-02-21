x = 5

print(x)

def hello():
    #likhne se global scope ka variable change ho jata hai
    global x
    x = 2
    y = 1
    print(f"the local x is {x}")
    print(f"the local y is {y}")

hello()
print(f"the global of x is {x}")

#code ki easy likho taaki 3-4 mhine baad aap samajh sake

