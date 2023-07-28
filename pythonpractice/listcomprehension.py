import time
a=[]
start=time.time()
for i in range(10**7):
    if i%2==0:
        a.append(i)
print("Execution time for the for loop is",time.time()-start)

start=time.time()
a=[i for i in range(10**7) if i%2==0]
print("Execution time for the for loop is",time.time()-start)
    