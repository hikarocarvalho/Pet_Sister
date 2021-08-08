arrayNum = [3,5,-4,8,11,1,-1,6]
targetSum = 10
def sumVerify(arrayValue):
    for i in arrayValue:
        for f in arrayValue:
                try:
                    if (arrayValue[i] + arrayValue[f]) == targetSum:
                        arrayValue.clear()
                except:
                    continue
    return arrayValue
print(sumVerify(arrayNum))
