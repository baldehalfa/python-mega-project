# myFile = open("fruits.txt")

# content = myFile.read()

# print(content)

with open("fruits.txt") as myFile:
    content = myFile.read()

print(content)
