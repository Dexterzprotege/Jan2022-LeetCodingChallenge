# Question: https://leetcode.com/problems/word-pattern/

# Solution:
class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        dic = {}
        arr = s.split()
        if len(arr) != len(pattern):
            return False
        for i in range(len(arr)):
            c = pattern[i]
            if c in dic:
                if dic[c] != arr[i]:
                    return False
            else:
                if arr[i] in dic.values():
                    return False
                dic[c] = arr[i]
        return True
      
# Verdict:
# Runtime: 20 ms, faster than 99.34% of Python3 online submissions for Word Pattern.
# Memory Usage: 14.3 MB, less than 55.31% of Python3 online submissions for Word Pattern.
