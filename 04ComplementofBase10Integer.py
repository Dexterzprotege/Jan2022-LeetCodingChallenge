# Question: https://leetcode.com/problems/complement-of-base-10-integer/

# Solution:
class Solution:
    def bitwiseComplement(self, n: int) -> int:
        b = str(bin(n))[2:]
        a = '1'*len(b)
        return int(a, 2) - int(b, 2)
      
# Verdict:
# Runtime: 53 ms, faster than 5.52% of Python3 online submissions for Complement of Base 10 Integer.
# Memory Usage: 14.3 MB, less than 38.43% of Python3 online submissions for Complement of Base 10 Integer.
