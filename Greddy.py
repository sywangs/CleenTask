import numpy as np
from PIL import Image
from pylab import *

def SortAllsqureByPrice(h,w,p):
    arr = np.array([h,w,p])
    row,colo = arr.shape
    price = []
    for i in range(colo):
        price.append(float(arr[2][i]/arr[0][i]*arr[1][i]))
    data = np.row_stack((arr,price)).T
    return data[data[:,2].argsort()]

def setMostExpensiveSqure(totalShape,Pos,W,H):
    result = []
    for num in range(len(sortedSqure)-1,-1,-1):
        squre = sortedSqure[num]
        if squre[0] <= H and squre[1] <= W:
            result = squre
            for i in range(int(squre[1])):
                for j in range(int(squre[0])):
                    totalShape[Pos[0] + j][Pos[1] + i] = num + 1
            break
        elif squre[0] <= W and squre[1] <= H:
            result = squre
            for i in range(int(squre[1])):
                for j in range(int(squre[0])):
                    totalShape[Pos[0] + i][Pos[1] + j] = num
            break
    return totalShape, result

def SetSqure(W,H,totalShape,Pos,Profit):
    totalShape,squre = setMostExpensiveSqure(totalShape,Pos,W,H)
    if not squre == []:
        allSqure.append(squre)
        Profit = Profit + squre[2]
        PosBottom = (int(Pos[0] + squre[0]),int(Pos[1]))
        totalShape, Profit = SetSqure(int(squre[1]),H - int(squre[0]),totalShape,PosBottom,Profit)

        PosRight = (int(Pos[0]),int(Pos[1] + squre[1]))
        totalShape, Profit = SetSqure(int(W - squre[1]),H,totalShape,PosRight,Profit)
    else:
        if not W == 0 and  not H == 0:
            Profit = Profit -1
    return totalShape,Profit


WInit = 20
HInit = 12

h = [5,5,7]
w = [5,4,8]
p = [8,3,15]
allSqure = []

totalShape = np.zeros((HInit,WInit))
sortedSqure = SortAllsqureByPrice(h,w,p)
Pos = (0,0)

totalShape,Profit = SetSqure(WInit,HInit,totalShape,Pos,0)
print "Profit is " + str(Profit)
for i in range(len(allSqure)):
    print (str(i) + "th squre: width " + str(allSqure[i][1]) + ",height " + str(allSqure[i][0]))
im = array(totalShape)
imshow(im)
show()


