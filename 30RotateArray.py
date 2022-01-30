# Question: https://leetcode.com/problems/rotate-array/

# ------------------------------------------------------------------------------------------------- #

# Solution 2: Reverse the solution
 class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        def reverse(nums, i, j):
            while i < j:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1
                j -= 1
        if nums == None or len(nums) < 2:
            return 
        k = k % len(nums)
        reverse(nums, 0, len(nums)-k-1)
        reverse(nums, len(nums) - k, len(nums) - 1)
        reverse(nums, 0, len(nums) - 1)

# Verdict:
# Runtime: 224 ms, faster than 75.75% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.5 MB, less than 83.32% of Python3 online submissions for Rotate Array.
  
# ------------------------------------------------------------------------------------------------- #

# Solution 1: Brute Force Solution
class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        if nums == None or len(nums) < 2:
            return 
        k = k % len(nums)
        while k:
            nums.insert(0, nums.pop())
            k -= 1
            
# Verdict:
# Runtime: 2180 ms, faster than 18.40% of Python3 online submissions for Rotate Array.
# Memory Usage: 25.5 MB, less than 83.32% of Python3 online submissions for Rotate Array.
# ------------------------------------------------------------------------------------------------- #
