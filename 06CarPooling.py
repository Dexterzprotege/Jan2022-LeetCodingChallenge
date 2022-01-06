# Question: https://leetcode.com/problems/car-pooling/

# Solution:
class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        routes = [0] * 1001
        for trip in trips:
            routes[trip[1]] += trip[0]
            routes[trip[2]] -= trip[0]
        
        i = 0
        while i < 1001 and capacity >=0:
            capacity -= routes[i]
            i += 1
            
        return capacity >= 0

# Verdict:
# Runtime: 131 ms, faster than 11.99% of Python3 online submissions for Car Pooling.
# Memory Usage: 14.6 MB, less than 98.45% of Python3 online submissions for Car Pooling.
