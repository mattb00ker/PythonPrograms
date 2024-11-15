def Fibon(idx):
    if idx <= 1:
        return idx
    else:
        return Fibon(idx-1)+Fibon(idx-2)
    

print(Fibon(39))