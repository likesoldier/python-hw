while(True):
    d,x = input().split(' ')
    d = int(d) 
    x = int(x) 
    
    b = ((6 * d) - (x + d)) // 2
    a = b + d
    
    print(str(a) + ' ' + str(b))