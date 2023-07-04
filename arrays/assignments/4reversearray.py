class Solution:
    # @param A : tuple of integers
    # @return a list of integers
    def solve(self, A):
        A_list=list(A)
        i = 0;
        j = len(A)-1
        while (i <= j):
            temp = A_list[i]
            A_list[i] = A_list[j]
            A_list[j] = temp
            i += 1
            j -= 1
        return A_list

