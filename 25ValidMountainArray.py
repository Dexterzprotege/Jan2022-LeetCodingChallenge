# Question: https://leetcode.com/problems/valid-mountain-array/

# Solution:
class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) < 3:
            return False
        inc = False
        dec = False
        for i in range(1, len(arr)):
            if arr[i] == arr[i-1]:
                return False
            
            if arr[i] > arr[i-1]:
                if dec == True:
                    return False
                inc = True
            if arr[i] < arr[i-1]:
                dec = True
        if inc == True and dec == True:
            return True
        else:
            return False

# Verdict:
# Runtime: 208 ms, faster than 59.96% of Python3 online submissions for Valid Mountain Array.
# Memory Usage: 15.5 MB, less than 61.89% of Python3 online submissions for Valid Mountain Array.
