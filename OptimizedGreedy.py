import numpy as np
from PIL import Image
from pylab import *



sumBefore = 0

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

def getMinPos(totalShape,Profit,sumBefore = 0):
    minPos = -1
    WNow = -1
    Hnow = -1
    (H,W) = totalShape.shape
    getMin = False
    for i in range( sumBefore + 1,W+H,1):
        movingW = 0
        movingH = i - movingW
        while movingH >= 0:
            if movingW < H and  movingH < W and totalShape[movingW,movingH] == 0:
                minPos = (movingW,movingH)
                getMin = True
                sumBefore = i
                break
            movingW = movingW + 1
            movingH = i - movingW
        if getMin:
            break
    if not minPos == -1:
        Hnow = H - minPos[0]
        for i in range(minPos[0],H,1):
            if totalShape[i][minPos[1]] == 0:
                Hnow = i - minPos[0] + 1
            else:
                break

        WNow = W - minPos[1]
        for i in range(minPos[1],W,1):
            if totalShape[minPos[0]][i] == 0:
                WNow = i - minPos[1] + 1
            else:
                break
    if WNow < min(w) or Hnow < min(h):
        i = 0
        if minPos == -1:
            return -1,-1,-1,-1,Profit
        else:
            while minPos[0] + i < H and totalShape[minPos[0] + i][minPos[1] - 1] != 0:
                for j in range(WNow):
                    totalShape[minPos[0] + i] [minPos[1] + j] = -1
                i += 1
            Profit = Profit - 1
            return getMinPos(totalShape,Profit)
    return minPos,Hnow,WNow,sumBefore,Profit


def SetSqure(W,H,totalShape,Pos,Profit,sumBefore):
    totalShape,squre = setMostExpensiveSqure(totalShape,Pos,W,H)
    if not squre == []:
        allSqure.append(squre)
        Profit = Profit + squre[2]
        nextPos,Hnow,WNow,sumBefore,Profit = getMinPos(totalShape,Profit)
        if not nextPos == -1:
            totalShape, Profit = SetSqure(WNow,Hnow, totalShape, nextPos, Profit,sumBefore)
    else:
        nextPos, Hnow, WNow, sumBefore,Profit = getMinPos(totalShape,Profit,sumBefore)
        if not nextPos == -1:
            totalShape, Profit = SetSqure(WNow, Hnow, totalShape, nextPos, Profit,sumBefore)
        pass

    return totalShape,Profit


WInit = 20
HInit = 12

h = [5,5,7]
w = [5,4,8]
p = [8,3,15]

totalShape = np.zeros((HInit,WInit))
sortedSqure = SortAllsqureByPrice(h,w,p)
Pos = (0,0)
allSqure = []
totalShape,Profit = SetSqure(WInit,HInit,totalShape,Pos,0,0)

for i in range(len(allSqure)):
    print (str(i) + "th squre: width " + str(allSqure[i][1]) + ",height " + str(allSqure[i][0]))
print Profit
im = array(totalShape)
imshow(im)
show()




