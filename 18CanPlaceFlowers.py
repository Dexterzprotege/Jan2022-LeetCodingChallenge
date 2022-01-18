# Question: https://leetcode.com/problems/can-place-flowers/

# ---------------------------------------------------------------------------------------------------- #
# Solution 1:
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        flowerbed = [0] + flowerbed + [0]
        zeroes = ''.join(map(str, flowerbed)).split('1')
        count = 0
        for zero in zeroes:
            count += (len(zero)-1) // 2
        return count >= n

# Verdict:
# Runtime: 332 ms, faster than 5.08% of Python3 online submissions for Can Place Flowers.
# Memory Usage: 15.5 MB, less than 8.05% of Python3 online submissions for Can Place Flowers.

# ---------------------------------------------------------------------------------------------------- #
# Solution 2:
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        N = len(flowerbed)
        flowerbed = [0] + flowerbed + [0]
        # flowerbed.append(0)
        # flowerbed.insert(0, 0)
        for i in range(1, N+1):
            if flowerbed[i] == flowerbed[i-1] == flowerbed[i+1] == 0:
                flowerbed[i] = 1
                n -= 1
            if n <= 0:
                return True
        return False

# Verdict:
# Runtime: 299 ms, faster than 8.94% of Python3 online submissions for Can Place Flowers.
# Memory Usage: 14.5 MB, less than 61.08% of Python3 online submissions for Can Place Flowers.

# ---------------------------------------------------------------------------------------------------- #
# Solution 3:
class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        count = 0
        for i in range(len(flowerbed)):
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i==len(flowerbed)-1 or flowerbed[i+1] == 0):
                flowerbed[i] = 1
                count += 1
        if count >= n:
            return True
        return False

# Verdict:
# Runtime: 322 ms, faster than 5.08% of Python3 online submissions for Can Place Flowers.
# Memory Usage: 14.6 MB, less than 61.08% of Python3 online submissions for Can Place Flowers.
# ---------------------------------------------------------------------------------------------------- #
