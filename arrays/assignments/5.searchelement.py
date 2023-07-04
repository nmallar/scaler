# You are given an integer T (number of test cases).
# You are given array A and an integer B for each test case.
# You have to tell whether B is present in array A or not.


def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    N=int(input())
    for i in range(0,N):
        list_n=list(int(num) for num in input().strip().split())
        A=int(input())
        list_n=list_n[1:]
        if A in list_n:
            print('1')
        else:
            print('0')
    return 0

if __name__ == '__main__':
    main()