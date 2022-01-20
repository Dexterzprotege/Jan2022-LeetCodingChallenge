# Question: https://leetcode.com/problems/koko-eating-bananas/
# ------------------------------------------------------------------------------------------------------------ #

# Solution 2: Binary Search O(N.LogM) M is max number in array
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatInTime(piles, mid, h):
            count = 0
            for i in piles:
                div = i//mid
                count += div
                if i%mid != 0:
                    count += 1
            return count <= h
        left = 1
        right = max(piles)
        ans = 0
        while left <= right:
            mid = left + (right-left) // 2
            if canEatInTime(piles, mid, h):
                right = mid - 1
            else:
                left = mid + 1
        return left

# Verdict:
# Runtime: 888 ms, faster than 12.47% of Python3 online submissions for Koko Eating Bananas.
# Memory Usage: 15.5 MB, less than 60.66% of Python3 online submissions for Koko Eating Bananas.

# ------------------------------------------------------------------------------------------------------------ #
# Solution 1: Brute from trying from 1 to answer O(NM) M is max number
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def canEatInTime(piles, mid, h):
            count = 0
            for i in piles:
                div = i//mid
                count += div
                if i%mid != 0:
                    count += 1
            return count <= h
        
        ans = 1
        while True:
            if canEatInTime(piles, ans, h):
                return ans
            else:
                ans += 1

# Verdict:
TLE
# ------------------------------------------------------------------------------------------------------------ #
