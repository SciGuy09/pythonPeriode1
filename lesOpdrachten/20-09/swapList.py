list = [5, 87, 43, -9]

def swapList(parameterLijst):
    if len(parameterLijst) > 1:
        parameterLijst[0], parameterLijst[1] = parameterLijst[1], parameterLijst[0]
        print(parameterLijst)

swapList(list)