# -*- coding: utf-8 -*-
def eq_add(numList):
    for i in range(2, len(numList)):
        if(numList[i] - numList[i-1] != numList[i-1] - numList[i-2]):   #等差判斷函數
            return False
    return True


def eq_ratio(numList):
    for i in range(2, len(numList)):
        if(numList[i] / numList[i-1] != numList[i-1] / numList[i-2]):   #等比判斷函數
            return False
    return True


rowNumInput = int(input())

for i in range(rowNumInput):
    numList = [int(numStr) for numStr in input().split(',')]
    # equal:
    # numListStr = input()
    # strList = numListStr.split(',')
    # numList = [int(str) for str in strList]
    # some ref info: https://stackoverflow.com/questions/5306079/python-how-do-i-convert-an-array-of-strings-to-an-array-of-numbers
    if (eq_add(numList) and eq_ratio(numList)):
        print("皆是")
    elif (eq_add(numList)):
        print("等差")
    elif (eq_ratio(numList)):
        print("等比")
    else:
        print("皆不是")
        
"""問題描述：
請撰寫一個程式；輸入第一行為t；第二行開始有t行測資，每行皆有一筆測資，每筆測資皆有n個數值x以「,」相隔，請判斷出每筆測資是等差或等比，若兩者皆是則輸出「皆是」，若兩者皆不是則輸出「皆不是」。

輸入說明：
輸入第一行為t；第二行開始有t行測資，每行皆有一筆測資，每筆測資皆有n個數值x以「,」相隔。

※ x ≥ 0
※ 不需要重新將讀入的組合進行排序

輸出說明：
請判斷出每筆測資是等差或等比，若兩者皆是則輸出「皆是」，若兩者皆不是則輸出「皆不是」。"""