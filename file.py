names =["adedoyin", "adeoluwa", "aderonke", "adebola", "adeseye"]

file = open("mynames.txt", "w") 
        
for name in names:
    file.write(str(name)+"\n")
file.close