def expendList(rawList, expendLength):  #大數加法，用來補0，先跑makeListSameLength算出長度絕對值後再跑此函式
    for i in range(expendLength):
        rawList.insert(0, 0)

    return rawList


def makeListSameLength(list_1, list_2):
    len_1 = len(list_1)
    len_2 = len(list_2)

    expendList(list_2 if len_1 > len_2 else list_1, abs(len_1-len_2))
    # 上面這行等價底下註解的程式碼，我只是不想寫if else呼叫同一個function但只是差在丟哪一個變數，所以寫成一行
    # if(len_1 > len_2):
    #     expendList(list_2, len_1 - len_2)
    # else:
    #     expendList(list_1, len_2 - len_1)

    return list_1, list_2


while(True):
    baseNum, strNum_1, strNum_2 = input().split(",")
    numList_1 = [int(digitStr) for digitStr in list(strNum_1)]
    numList_2 = [int(digitStr) for digitStr in list(strNum_2)]
    baseNum = int(baseNum)
    if(len(numList_1) != len(numList_2)):
        numList_1, numList_2 = makeListSameLength(numList_1, numList_2)

    outputList = []

    overflowFlag = False
    for i in range(len(numList_1)-1, -1, -1):
        digitResult = numList_2[i] + numList_1[i]

        if(overflowFlag == True):
            digitResult += 1

        if(digitResult >= baseNum):
            overflowFlag = True
            digitResult -= baseNum
        else:
            overflowFlag = False

        outputList.append(str(digitResult))

    if(overflowFlag == True):
        outputList.append("1")

    print("".join(reversed(outputList)))