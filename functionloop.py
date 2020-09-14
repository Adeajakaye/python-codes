Temperature=[10,-20,-289,100]

def celsius_to_fahrehient(celsius):
    fahrehient = celsius * 9/5 + 32
    return fahrehient

if c < -273.15:
    print("that temprature is impossible")
else:
    fahrehient = celsius * 9/5 + 32
    print(fahrehient)

for t in Temperature:
    print(celsius_to_fahrehient(t))