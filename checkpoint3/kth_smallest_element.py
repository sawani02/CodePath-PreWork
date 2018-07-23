#Question: Find the kth smallest element in an unsorted array of non-negative integers.
#Problem link: https://www.interviewbit.com/problems/kth-smallest-element-in-the-array/

class Solution:
    # @param A : tuple of integers
    # @param B : integer
    # @return an integer
    def kthsmallest(self, A, B):
        #sort
        sorted_A = sorted(A)
        return sorted_A[B - 1]
