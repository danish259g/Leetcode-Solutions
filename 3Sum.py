"""
Problem 15 - 3Sum
Link - https://leetcode.com/problems/3sum/
"""

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        nums.sort()
        for k in range(len(nums)):
            if k > 0 and nums[k] == nums[k - 1]:  # do not fixate on same number again
                k += 1
                continue
            complement = -nums[k]
            i = k + 1
            j = len(nums) - 1
            while i < j:
                if nums[i] + nums[j] > complement:
                    j -= 1
                elif nums[i] + nums[j] < complement:
                    i += 1
                else:  # sum is equal to complement <=> 3sum = 0
                    res.append([nums[k], nums[i], nums[j]])
                    i += 1
                    while nums[i] == nums[i - 1] and i < j:
                        i += 1

        return res