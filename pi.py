
def minInitialEnergy(arr):
    n = len(arr)    
    initMinEnergy = 0
    currEnergy = 0
    flag = 0
    for i in range(n):
        currEnergy += arr[i]
        if currEnergy <= 0 :
            initMinEnergy += (abs(currEnergy) +1)
            currEnergy = 1
            flag = 1
    return 1 if flag == 0 else initMinEnergy