# Question: https://leetcode.com/problems/largest-rectangle-in-histogram/

# ------------------------------------------------------------------------------------------------------------- #

# Solution 2: Stack: Find min on left and right:
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        i = 0
        stack = []
        while i < n:
            if len(stack) == 0 or heights[stack[-1]] <= heights[i]:
                stack.append(i)
                i += 1
            else:
                top = stack[-1]
                stack.pop()
                if len(stack)==0:
                    area= max(area, heights[top]*i)
                else:
                    width = i - stack[-1] -1
                    area= max(area, heights[top]*width)
        while stack:
            top = stack[-1]
            stack.pop()
            if len(stack)==0:
                area= max(area, heights[top]*i)
            else:
                width = i - stack[-1] -1
                area= max(area, heights[top]*width)
        return area

# Verdict:
# Runtime: 1562 ms, faster than 9.43% of Python3 online submissions for Largest Rectangle in Histogram.
# Memory Usage: 28.4 MB, less than 29.33% of Python3 online submissions for Largest Rectangle in Histogram.

# ------------------------------------------------------------------------------------------------------------- #

# Solution 1: Iterative: Find min on left and right:
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        area = 0
        for i in range(n):
            p1 = i-1 # First smaller point on the left
            p2 = i+1 # First smaller point on the right
            while p1 >= 0:
                if heights[p1] < heights[i]:
                    break
                p1 -= 1
            while p2 <= n-1:
                if heights[p2] < heights[i]:
                    break
                p2 += 1
            width = p2 - p1 -1
            height = heights[i]
            area = max(area, width*height)
        return area

# Verdict
TLE

# ------------------------------------------------------------------------------------------------------------- #
