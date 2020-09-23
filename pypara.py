
path = 'paragraph_1.txt' #user_input("What is the name of the file you want to consider? ")

with open(path, "r") as f:
    para = [x for x in f]

print(para)
