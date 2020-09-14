temperatue= [10,-20,-289,100]

def Celcius_to_fahrehient(Celcius):
    fahrehient = Celcius * 9/5 + 32
    return fahrehient



if Celcius < -273.5:
    print("that temperature is impossible")
else:
    print(fahrehient)
for t in temperatue:
    print(Celcius_to_fahrehient(100)) 