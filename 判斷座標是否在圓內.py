# -*- coding: utf-8 -*-
def isOnOverlap(twoCircle, point):  #檢查有沒有在雙圓交點上
    if (isInCircle(twoCircle[0:3], point) and isInCircle(twoCircle[3:], point)): 
        #[0:3]索引0到索引2(不包括索引3)的字元，[3:]索引3到索引n-1，詳見py課本3-18
        # 因為圓周上所有也等同在圓內
        # 同時在圓A以及圓B內的事件只可能發生在圓A及圓B的交點
        return True
    return False


def isInCircle(circle, point):      #檢查有沒有在圓內
    # circle: [x, y, r]
    # point: [x, y]

    # another ver. of if() condition
    # deltaX = (circle[0] - point[0])
    # deltaY = (circle[1] - point[1])
    # if (deltaX ** 2 + deltaY ** 2 <= circle[2] ** 2):
    #    return True

    if ((circle[0] - point[0])**2 + (circle[1] - point[1])**2 <= circle[2] ** 2):
        # 座標距離公式
        return True
    return False


twoCircleXYR = [int(numStr) for numStr in input().split(',')]
# x1 y1 r1 x2 y2 r2

inputRowNum = int(input())

for i in range(inputRowNum):
    at_overlap = 0
    not_in_both = 0
    in_first_circle = 0
    in_second_circle = 0

    inputPointList = [int(numStr) for numStr in input().split(',')]

    for i in range(len(inputPointList) // 2):
        currentPoint = inputPointList[2 * i:2 * i + 2]
        # 第2*i 跟 2*i+1 個的陣列切片
        if(isOnOverlap(twoCircleXYR, currentPoint)):
            at_overlap += 1
            continue
        elif(isInCircle(twoCircleXYR[0:3], currentPoint)):
            in_first_circle += 1
            continue
        elif(isInCircle(twoCircleXYR[3:], currentPoint)):
            in_second_circle += 1
            continue
        else:
            not_in_both += 1

    print(at_overlap, not_in_both, in_first_circle, in_second_circle,sep=",") #sep=   <--使用甚麼填間隔
    
    
"""問題描述：
請撰寫一個程式，輸入第一行為兩個圓的座標及半徑，依序分別為x1, y1, r1, x2, y2, r2，其中x代表x軸位置，y代表y軸位置，r代表圓的半徑；第二行為一個整數(int)t；第三行開始共有t行測資，每行有2n筆由「,」隔開的數值，其代表要測試的座標點，分別為x1, y1, x2, y2, x3, y3....., xn, yn。請輸出每行測資的結果，分別為「座標在兩圓交集處、座標不在任一圓內、座標只在第一個圓內、座標只在第二個圓內」的數量。

輸入說明：
輸入第一行為兩個圓的座標及半徑，依序分別為x1, y1, r1, x2, y2, r2，其中x代表x軸位置，y代表y軸位置，r代表圓的半徑；第二行為一個整數(int)t；第三行開始共有t行測資，每行有2n筆由「,」隔開的數值，其代表要測試的座標點，分別為x1, y1, x2, y2, x3, y3....., xn, yn。

輸出說明：
請輸出每行測資的結果，分別為「座標在兩圓交集處、座標不在任一圓內、座標只在第一個圓內、座標只在第二個圓內」的數量。"""