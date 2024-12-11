"""
Problem - 128 Longest Consecutive Sequence
Link - https://leetcode.com/problems/longest-consecutive-sequence/
"""

class Solution(object):
    def longestConsecutive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        
        longest = 0
        nums_set = set(nums)

        for num in nums_set:
            if (num - 1) not in nums_set: # n is the start of some sequence 
                length = 1
                while (num + length) in nums_set:
                    length += 1 
                longest = max(longest, length)
        
        return longest 