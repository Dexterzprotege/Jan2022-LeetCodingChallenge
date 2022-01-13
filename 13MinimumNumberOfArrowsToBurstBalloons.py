# Question: https://leetcode.com/problems/minimum-number-of-arrows-to-burst-balloons/

# Solution:
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort(key = lambda x: x[1])
        arrow = 1
        end = points[0][1]
        for i in range(1, len(points)):
            if points[i][0] > end:
                arrow += 1
                end = points[i][1]
        return arrow

# Verdict:
# Runtime: 1224 ms, faster than 93.37% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
# Memory Usage: 59.2 MB, less than 10.57% of Python3 online submissions for Minimum Number of Arrows to Burst Balloons.
