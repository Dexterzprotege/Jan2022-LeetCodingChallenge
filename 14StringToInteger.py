# Question: https://leetcode.com/problems/string-to-integer-atoi/

# Solution:
class Solution:
    def myAtoi(self, s: str) -> int:
        ls = list(s.strip())
        if len(ls) == 0: return 0
        sign = -1 if ls[0] == '-' else 1
        if ls[0] in ['-','+'] : del ls[0]
        ret, i = 0, 0
        while i < len(ls) and ls[i].isdigit() :
            ret = ret*10 + ord(ls[i]) - ord('0')
            i += 1
        return max(-2**31, min(sign * ret, 2**31-1))
      
# Verdict:
# Runtime: 36 ms, faster than 69.33% of Python3 online submissions for String to Integer (atoi).
# Memory Usage: 14.2 MB, less than 81.95% of Python3 online submissions for String to Integer (atoi).
