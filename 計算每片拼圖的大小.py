while(True):
    w, h, min_w, min_h = input().split(' ')
    w = int(w)
    h = int(h)
    min_w = int(min_w)
    min_h = int(min_h)
    x = w // min_w
    y = h // min_h
    
    print(str(round((w / x),3)) + ' ' + str(round((h / y),3)))
