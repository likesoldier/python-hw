def Delta(cut):  
    cut1 = sorted(cut,reverse = False)  
    if (cut1[0] + cut1[1] > cut1[2]):  
        return True  
    else:  
        return False  
      
t = int(input())  
for i in range(t):  
    cando = 0  
    cannotdo = 0  
    int_nums = list(map(int,input().split(',')))  
    for j in range(0,len(int_nums)//3):  ##j每次+1 ex:j=0>>0~2，j=1>>3~6  
        cut = int_nums[j*3:(j+1)*3]  ##陣列切片
        if Delta(cut):  
            cando += 1  
            continue  
        else:  
            cannotdo += 1  
            continue  
    print(cando,cannotdo,sep=',')  
