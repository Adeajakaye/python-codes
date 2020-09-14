file = open("number.txt","w")
numbers = [1,2,3,4,5]
for i in numbers:
    file.write(str(i)+"\n")
file.close()