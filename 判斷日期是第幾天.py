import datetime

def TimeDate(cut):
    if (cut[0] == 0):
        cut[0] = 1
    try:
        d1 = datetime.date(cut[0],1,1)
        d2 = datetime.date(cut[0],cut[1],cut[2]) 
        day_plus = (abs(d2-d1).days) + 1
        print(day_plus)
    except:
        print('error')

while True:
    int_ymd = list(map(int,input().split(' ')))  
    for i in range(0,len(int_ymd)//3):  ##i每次+1 ex:i=0>>0~2，i=1>>3~6  
        cut = int_ymd[i * 3:(i + 1) * 3]           
        TimeDate(cut)  
        
