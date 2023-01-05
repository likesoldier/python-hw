while(True):
    inputStrList = input().split(',')
    # result of input already is string(), no need to assign dataType
    # but it's a good habit tho
    for inputStr in inputStrList:
        # in this for loop, we gonna processing each substring in line of user input
        outputStr = ""
        for strChar in list(inputStr):
            if(ord(strChar) > 47 and ord(strChar) < 58): #ASCII
                outputStr += strChar
        print(outputStr)