
#continous sum query
#There are A beggars sitting in a row outside a temple. Each beggar initially has an empty pot. When the devotees come to the temple, they donate some amount of coins to these beggars. Each devotee gives a fixed amount of coin(according to their faith and ability) to some K beggars sitting next to each other.

# Given the amount P donated by each devotee to the beggars ranging from L to R index, where 1 <= L <= R <= A, find out the final amount of money in each beggar's pot at the end of the day, provided they don't fill their pots by any other means.
# For ith devotee B[i][0] = L, B[i][1] = R, B[i][2] = P, Given by the 2D array B

#input
# A = 5
# B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]

# Output
# 10 55 45 25 25
#Solution : 
# Instead of updating each beggar ranging from i to j, we could update index i with +S and index j + 1 with -S, where S is a donation made by some devotee. So if you want to know the number of coins taken by kth beggar, you just need to find the prefix sum of all the values(coins) from 1 to k(Try to prove it by yourself that values between i to j contains +S as you are doing prefix sum).
# This technique is known as difference array and is very helpful in problems which involves range updates.

# Time complexity : O(A+n) , where n denotes the size of B

# Space complexity : O(A)

# Example:
# N = 5, D = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
# Initial array: [0, 0, 0, 0, 0]

# After first devotee, if we update i = 1 with +10 and j + 1 = 3 with -10, we get [10, 0, -10, 0, 0]. Now note that if you add 10 to 1st index and subtract 10 with 3rd index and do a prefix sum at every array element, you will get +10 at 1st and 2nd.
# After second devotee, if we update i = 2 with +20 and j + 1 = 4 with -20, we get [10, 20, -10, -20, 0].
# Similarly, after third devotee, if we update i = 2 with +25 and j + 1 = 6 with -25, we get [10, 45, -10, -20, 0].
# Now, if we calculate the prefix sum at every index, we get [10, 55, 45, 25, 25].

A= 5
B = [[1, 2, 10], [2, 3, 20], [2, 5, 25]]
sum=[]
for i in range(0,A):
    sum.append(0)
print(sum)
for n in range(0,len(B)):
    i=B[n][0]
    j=B[n][1]
    D=B[n][2]
    #for x in range(i-1,j+1-1):
    sum[i-1]+=D
    if j < A:
        sum[j]+=-D
            
print(f"sum before prefix sum {sum}")
psum=[]
psum.append(sum[0])

for i in range(1,len(sum)):
    psum.append(psum[i-1]+sum[i])

print(f"prefix sum= {psum}")

        
        
    