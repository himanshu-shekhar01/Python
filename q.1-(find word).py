# f = open("/Users/himanshu/Documents/python/day49(file.io)/poem.txt","r")
# print(f.read())
# f.close()

def file_contains_word(file_path, word):
    with open("/Users/himanshu/Documents/python/day49(file.io)/poem.txt", 'r') as file:
        text = file.read()
        words = text.lower().split()
        print
        return word.lower() in words

file_path = "/Users/himanshu/Documents/python/day49(file.io)/poem.txt"
word = "twinkle"
print(f"Does the file '{file_path}' contain the word '{word}'? {file_contains_word(file_path, word)}")




