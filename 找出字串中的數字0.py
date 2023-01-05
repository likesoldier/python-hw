while(True):
    strLIST = input().split(',')
    for i in strLIST:
        list2 = ""
        sum = 0
        for j in list(i):
            if j == '1' or j == '2' or j == '3' or j == '4' or j == '5' or j == '6' or j == '7' or j == '8' or j == '9' or j == '0':
                list2 += j
                sum += 1
            else:
                continue
        print(list2)