def string_length(strings):
    return len(strings)
strings =str(input("please enter your details: "))

if type(strings) == int:
    print("intergers dont have length")
else:
    print(len(strings))
