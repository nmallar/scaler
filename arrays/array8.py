#given an array of N elements and a range of start , end, and a flag
#if flag is O return sum of all odd numbers in given range
#if flag is E return sum of all even numbers in given range

arr=[1,2,3,4,5,6,7,8,9,10]
Q=4
s=[0,2,1,4]
e=[3,4,5,6]
flag=['E','O','E','O']
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
        
print(f"Original array {arr}")
print(f"Even number PS : {pse}")
print(f"Odd number PS {pso}")


for i in range(0,Q):
    start=s[i]
    end=e[i]
    if flag[i]=='E':
        if start==0:
            print(pse[end])
        else:
            print(pse[end]-pse[start-1])

    else:
        if start==0:
            print(pso[end])
        else:
            print(pso[end]-pso[start-1])