#Question: Given an array, find the next greater element G[i] for every element A[i] in the array. 
#The Next greater Element for an element A[i] is the first greater element on the right side of A[i] in array. 
#Question link:https://www.interviewbit.com/problems/nextgreater/

class Solution:
    # @param A : list of integers
    # @return a list of integers
    def nextGreater(self, A):
        nge_stack = []
        output = []
        for num in A[::-1]:
            nge = -1
            while nge_stack:
                test_num = nge_stack.pop()
                if test_num > num:
                    nge = test_num
                    nge_stack.append(nge)
                    break

            output.append(nge)
            nge_stack.append(num)

        return output[::-1]
