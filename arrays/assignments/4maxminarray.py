# 3 max min array
# Take input an array A of size N and write a program to print maximum and minimum elements of the input.
# The only line of the input would contain a single integer N that represents the length of the array 
# followed by the N elements of the input array A.


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    

    A = list(map(int, input().strip().split()))
    
    A=A[1:]
    max=A[0]
    min=A[0]
    for i in range(1,len(A)):
        if A[i]>max:
            max=A[i]
        if A[i]<min:
            min=A[i]
    print(f"{max} {min}")
   
    return 

if __name__ == '__main__':
    main()