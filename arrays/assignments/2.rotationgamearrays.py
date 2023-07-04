#Given an integer array A of size N and an integer B, you have to print the same array after rotating it B times towards the right.

def reverse(A, start,end):
    i=start
    j=end
    while(i<=j):
        temp=A[i]
        A[i]=A[j]
        A[j]=temp
        i+=1
        j-=1
    return

def rotate(A,K):
    K=K%len(A)
    reverse(A,0, len(A)-1)
    reverse(A,0,K-1)
    reverse(A,K,len(A)-1)
    10
def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    numlist=list(int(num) for num in input().strip(',').split())
    A=numlist[1:]
    K=int(input())
    rotate(A,K)
    for i in range(0,len(A)):
        print(A[i],end=" ")
    return 0

if __name__ == '__main__':
    main()