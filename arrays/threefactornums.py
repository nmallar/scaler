import math
arr=[1,8,12,5,5]
Q=4
s=[2,1,3,4]
e=[3,5,4,5]
ls=[]

for c in range(Q):
    
    count=0
    for num in range(s[c]-1,e[c]):
        factors=0
        x=arr[num]
        
    
        
        for i in range(1,int(math.sqrt(x))+1):
            #print(f"sqrt {int(math.sqrt(x))}")
            if x%i==0:
                if i != x/i:
                    factors+=2
                else:
                    factors+=1
        if factors>=3:
            count+=1
    ls.append(count)
print(ls)    
            
            
