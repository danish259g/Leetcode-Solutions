"""
Problem - Search In Rotated Sorted Array
Link - https://leetcode.com/problems/search-in-rotated-sorted-array/
"""

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """
        
        l, r = 0, len(nums) - 1

        while l <= r:
            mid = l + (r - l) // 2
            
            # Check if the middle element is the target
            if nums[mid] == target:
                return mid
            
            # Determine if the left half is sorted
            if nums[l] <= nums[mid]:
                if nums[l] <= target < nums[mid]:  # Target in sorted left half
                    r = mid - 1
                else:  # Target in the other half
                    l = mid + 1
            else:  # Right half is sorted
                if nums[mid] < target <= nums[r]:  # Target in sorted right half
                    l = mid + 1
                else:  # Target in the other half
                    r = mid - 1
        
        return -1  # Target not found