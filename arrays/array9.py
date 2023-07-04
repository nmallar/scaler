#Given an array of N elements count the number of special indexes in the array
#special index : an index after removing which 
# sum of all odd index elements = sum of all even index elements



#arr=[1,2,3,4,5,6,7,8,9,10]
arr=[4,3,2,7,6,-2] # 3 2 7 6 -2 : Evensum :  8 Oddsum : 8 for i=0
pse=list()
pso=list()
pse.append(arr[0])
pso.append(0)
for i in range(1,len(arr)):
    if i%2==0:
        pse.append(pse[i-1]+arr[i])
        pso.append(pso[i-1])
    else:
        pso.append(pso[i-1]+arr[i])
        pse.append(pse[i-1])
        

specialIndexCount=0
end=len(arr)
for i in range(0,end-1):
    if i==0:
        sumeven=pse[end-1]-pse[0]
        sumodd=pso[end-1]-pso[0]
    else:
        sumeven=pse[i-1]+ (pso[end-1]-pso[i])
        sumodd=pso[i-1]+ (pse[end-1]-pse[i])
    if sumeven==sumodd:
        specialIndexCount+=1
    print(f" Value of i is : {i} - Even Sum : {sumeven}  - Odd Sum : {sumodd}")
        
print(f" The number of special indexes in this array are: {specialIndexCount}")
    