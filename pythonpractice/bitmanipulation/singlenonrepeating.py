# all elements are repeating twice except one unique

A=[12,13,9,13,12,14,15,14,16,18,15,16,18]

result=A[0]
for num in A[1:]:
    result=result^num
   

print(result)