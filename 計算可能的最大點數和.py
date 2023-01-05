while(True):
    inputList = [int(num_str) for num_str in input().split(' ')]
    inputList.sort()
    
    if len(inputList) <= 1:
        print('0')
        continue
    elif len(inputList) == 2:
        print(inputList[0])
        continue
          
    List = inputList[(len(inputList)//3):]
    print(List)   
    if len(List) % 2 != 0:
        sum = 0   
        for i in range(1,len(List),1):          
            
                sum += i
        print(sum)
    else:       
        sum = 0
        for i in range(len(List)):
            if 
                sum += i
        print(sum)
         
#cut = (list(cut) for cut in List[i * 2:(i + 1) * 2])
#for j in cut():           
#sum += j