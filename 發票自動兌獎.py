# -*- coding: utf-8 -*-
rowNumInput = int(input()) #後續行數輸入(幾組側資)
prizeNum = input()         #發票編號輸入

prize = [0, 0, 0, 500, 2000, 5000, 50000, 300000, 1000000] #獎金設置(+設置後0、1、2碼相同獲得0$，完整化)

prizeAmount = 0     #獎金金額初始化

for i in range(rowNumInput):
    invoiceNumList = input().split(',')  #編號列表

    for invoiceNum in invoiceNumList:    
        tempAmount = 0                   

        for j in range(3, 9):
            if(prizeNum[-j:] == invoiceNum[-j:]):
                tempAmount = prize[j]  #or prize前3個0拿掉，改成[j-3]

        prizeAmount += tempAmount

print(f"Ans: {prizeAmount}")


"""問題描述：
請撰寫一個程式，讀入中獎號碼與兌獎號碼，輸入第一行為t代表總共有t組測資，第二行會是中獎號碼，第三行開始共有t筆測資，而每筆測資中又有n個號碼以「,」隔開，請讀入以上資訊後將中獎金額總和按照格式輸出。

後3碼相同時獲得500元
後4碼相同時獲得2,000元
後5碼相同時獲得5,000元
後6碼相同時獲得50,000元
後7碼相同時獲得300,000元
後8碼相同時獲得1,000,000元

輸入說明：
輸入第一行為t代表總共有t組測資，第二行會是中獎號碼，第三行開始共有t筆測資，而每筆測資中又有n個號碼以「,」隔開。

輸出說明：
請讀入以上資訊後將中獎金額總和按照格式輸出，若總和為0時改為輸出「Error」。"""