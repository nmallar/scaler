# given an array of size N and has all elements from 1 to N+2,
# two elements are missing
# e g. N=4 A=[1,3,4,5] missing (2,6)

A = [1, 3, 4, 5]

val = 0

for i in range(1, len(A) + 3):
    val = val ^ i

for num in A:
    val = val ^ num

pos = -1
for i in range(31):
    if (val >> i) & 1 == 1:
        pos = i
        break

set = 0
unset = 0

for num in A:
    if (num >> pos) & 1 == 1:
        set = set ^ num
    else:
        unset = unset ^ num

for num in range(1, len(A) + 3):
    if (num >> pos) & 1 == 1:
        set = set ^ num
    else:
        unset = unset ^ num


print(f"{set} {unset}")
