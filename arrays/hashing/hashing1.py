#hashing
#1. Find the frequency of numbers.
# Given an array of N elements and Q queries for each uery find the frequency of each element in array

A=[2,6,3,8,2,8,2,3,8,10]
Q=[4, 2,8,3,5]
print(f"Original array is {A}")
dict={}
queries=Q[0]
elements=Q[1:]

for i in A:
    dict[i]=1+dict.get(i,0)

for i in range(0,len(Q)):
    if i in dict:
        print(f"{i} appears {dict[i]} times ")
print(dict.items())