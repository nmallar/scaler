#6. Given an array of N elements
# and Q queries of the format start and end, 
# Return the sum of elemtns from index start to end
#PREFIX SUM

arr=[10,20,30,40,50,60,70]
Q=4
s=[0,2,3,4]
e=[3,4,5,76]

print(arr)

#brute force method
# for i in range(0,Q):
#     start=s[i]
#     end=e[i]
#     sum=0
#     while(start<end):
#         sum=sum+arr[start]
#         start+=1
#     print(sum)

#using prefix sum

ps=list()
ps.append(arr[0])
for i in range(1,len(arr)):
    ps.append(ps[i-1]+arr[i])
    
for i in range(0,Q):
    start=s[i]
    end=e[i]
    if start==0:
        print(ps[end])
    else:
        print(ps[end]-ps[start-1])