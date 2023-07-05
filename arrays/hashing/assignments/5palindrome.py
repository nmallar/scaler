
# Given a string A consisting of lowercase characters.

# Check if characters of the given string can be rearranged to form a palindrome.

# Return 1 if it is possible to rearrange the characters of the string A such that it becomes a palindrome else return 0.


#A= "ttyya"
A='inttnikjmjbemrberk'
dict={}

for char in A:
    if char in dict:
        dict[char]=1+dict.get(char)
    else:
        dict[char]=1
count=0

for (key,value) in dict.items():
    print(count)
    print(f"Key : {key} - Value-{value}")
    
    if value%2!=0:
        count+=1

if count>1:
    print("Not possible to rearrange as  a palindrome")
else:
    print("Its possible to rearrange as palindrome")