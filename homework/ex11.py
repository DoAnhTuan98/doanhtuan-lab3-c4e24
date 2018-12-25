
# a = [100,120]
# b = [140,60,100,200]
def is_inside(a,b):
    if  b[0]<a[0]<b[0]+b[2]:
        if b[1] < a[1] < b[1]+b[3]:
         return True
    else:
        return False
    
        
t=is_inside([100,120],[140,60,0,0])

t1 = is_inside([200,120],[140,60,100,200])




