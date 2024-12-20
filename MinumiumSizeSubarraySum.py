"""
Problem - 209 Minimum Size Subarray Sum
Link - https://leetcode.com/problems/minimum-size-subarray-sum/
"""


class Solution(object):
    def minSubArrayLen(self, target, nums):
        """
        :type target: int
        :type nums: List[int]
        :rtype: int
        """

        left = 0
        right = 0
        shortest = 0
        curr = 0

        while right < len(nums):
            # advance right-idx
            while curr < target and right < len(nums):
                curr += nums[right]
                right += 1
                # advance left-idx
            while curr >= target and left <= right:
                # if needed, update shortest
                if shortest == 0 or right - left < shortest:
                    shortest = right - left
                curr -= nums[left]
                if left < right:
                    left += 1

        return shortest