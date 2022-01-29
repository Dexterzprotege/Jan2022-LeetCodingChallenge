# Question:

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

# Solution 1: Iterative: Find min on left and right:

# Verdict
