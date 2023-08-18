
# all elements appear twice except two unique elements that occur only once.

A=[10,8,8,9,12,6,11,10,6,12,17,9]


ans=0
for num in A:
    ans=ans^num
    
pos=-1
for i in range(31):
    if (ans>>i) & 1 ==1:
        pos=i
        break

set=0
unset=0

for num in A:
    if (num>>pos) & 1==1:
        set=set^num
    else:
        unset=unset^num 

print(f"{set} : {unset}")