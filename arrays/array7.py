#Given an array , return if there is an equalibrium index in the array
# equilibrium index= index whose sum of all elements on left= sum of all elements on right
# arr=[1,2,3,4,8,10] has an equilibrium index of 4 (value 8) because sum of all elements on left of index 4 = 10 and sum of all elements to right of index 4 is also 10


def equilibriumIndexExists(arr,ps):
    for i in range(0,len(arr)):
        if i==0:
            leftsum=0
        else:
            leftsum=ps[i-1]
        rightsum=ps[len(arr)-1]-ps[i]
        print(f" i is {i} - leftsum is {leftsum} - rightsum is {rightsum}")
        if leftsum==rightsum:
            print(f"Equilibirum index is {i}")
            return True
    return False


#arr=[1,2,3,4,8,10]
#arr=[10,2,-2,5,-5]
arr=[7,3,4,5,14]
#build prefix sum
ps=list()
ps.append(arr[0])
for i in range(1,len(arr)):
    ps.append(ps[i-1]+arr[i])
    

print(equilibriumIndexExists(arr,ps))