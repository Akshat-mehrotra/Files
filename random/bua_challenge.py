counter  = 2
b = []
c = 1
while(len(b)<=50):
    for d in range(c):
        if d!=1 and d!=0:
            if c%d != 0:
                b.append(d)
    c+=1        

print(b)            
            
    
