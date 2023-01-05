while True: 
    numList = input().split(' ')    
    total = 0
    for num in range(0,len(numList)):
        numList[num] = int (numList[num])
        if numList[num] > 1:
            for i in range(2,numList[num] // 2 + 1):
                if (numList[num] % i) == 0:
                    break
            else:
                total += 1
        else:
            total += 0
    print(total)