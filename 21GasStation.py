# Question: https://leetcode.com/problems/gas-station/

# Solution:
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        total = 0
        start = 0
        for i in range(len(gas)):
            total += (gas[i] - cost[i])
            if total < 0:
                total = 0
                start = i+1
        return start

# Verdict:
# Runtime: 436 ms, faster than 99.39% of Python3 online submissions for Gas Station.
# Memory Usage: 18.8 MB, less than 75.25% of Python3 online submissions for Gas Station.
