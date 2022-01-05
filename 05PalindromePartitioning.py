# Question: https://leetcode.com/problems/palindrome-partitioning/

# Solution1: Backtracking
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        def DFS(start, end, curr):
            if start == end:
                result.append(curr[:])
            for i in range(start, end):
                temp = s[start: i+1]
                if temp == temp[::-1]:
                    curr.append(temp)
                    DFS(i+1, end, curr)
                    curr.pop()
        
        result = []
        DFS(0, len(s), [])
        return result

# Verdict
# Runtime: 1026 ms, faster than 9.33% of Python3 online submissions for Palindrome Partitioning.
# Memory Usage: 31.2 MB, less than 15.41% of Python3 online submissions for Palindrome Partitioning.
