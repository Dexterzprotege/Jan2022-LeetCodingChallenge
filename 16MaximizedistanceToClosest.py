# Question: https://leetcode.com/problems/maximize-distance-to-closest-person/

# Solution:
class Solution:
    def maxDistToClosest(self, seats: List[int]) -> int:
        dist = float('-inf')
        j = -1
        if seats[0] == 1:   j = 0
        n = len(seats)
        for i in range(n):
            if seats[i] == 1:
                if j == -1:
                    dist = max(dist, i)
                else:
                    dist = max(dist, (i-j)//2)
                j = i
        if seats[n-1] == 0:
            dist = max(dist, n - 1 - j)
        return dist

# Verdict:
# Runtime: 227 ms, faster than 13.33% of Python3 online submissions for Maximize Distance to Closest Person.
# Memory Usage: 14.8 MB, less than 25.91% of Python3 online submissions for Maximize Distance to Closest Person. 
