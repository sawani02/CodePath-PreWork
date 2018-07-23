#Question: Given an unsorted array of integers, find the length of the longest consecutive elements sequence.
#Question link: https://www.interviewbit.com/problems/longest-consecutive-sequence/
class Solution:
    # @param A : tuple of integers
    # @return an integer
    def longestConsecutive(self, A):
        hash_A = {num: True for num in A}
        long_con_seq = 0

        for num in hash_A:
            if hash_A[num]:
                length = 1
                hash_A[num] = False

                higher = num + 1
                while higher in hash_A:
                    length += 1
                    hash_A[higher] = False
                    higher += 1

                lower = num - 1
                while lower in hash_A:
                    length += 1
                    hash_A[lower] = False
                    lower -= 1

                long_con_seq = max(long_con_seq, length)

        return long_con_seq
