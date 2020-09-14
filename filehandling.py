file= open("fruit.txt","r")
print(type(file))

content = file.readlines()
file.close()
for i in content:
    print(len(i.strip()))


file = open("fruit.txt","r")
content = file.read()
print(content)