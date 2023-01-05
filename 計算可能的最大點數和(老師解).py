while True: 
    num = list(map(int,input().split())) 
    a = 0 
    b = 0  
    c = 0 
    while(num != []): 
        try: 
            temp = max(num) 
            a += temp 
            num.remove(temp) 
            temp = max(num) 
            b += temp 
            num.remove(temp) 
            temp = min(num) 
            c += temp 
            num.remove(temp) 
        except: 
            temp = 0 
    print(b)  