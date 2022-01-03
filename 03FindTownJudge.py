# Question: https://leetcode.com/problems/find-the-town-judge/

# Solution:
class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        arr = [0]*(n+1)
        for i in trust:
            p1, p2 = i[0], i[1]
            arr[p1] -= 1
            arr[p2] += 1
        for i in range(1, n+1):
            if arr[i] == n-1:
                return i
        return -1

# Verdict:
# Runtime: 1292 ms, faster than 5.17% of Python3 online submissions for Find the Town Judge.
# Memory Usage: 19 MB, less than 65.18% of Python3 online submissions for Find the Town Judge.
