# Question: https://leetcode.com/problems/add-binary/

# Solution:
class Solution:
    def addBinary(self, a: str, b: str) -> str:
        ans = ""
        carry = 0
        i, j = len(a)-1, len(b)-1
        while i >= 0 or j >= 0:
            summ = carry
            if i>=0:
                summ += int(a[i])
                i -= 1
            if j >= 0:
                summ += int(b[j])
                j -= 1
            ans += str(summ % 2)
            carry = summ//2
        if carry != 0:
            ans += str(carry)
        return ans[::-1]
      
# Verdict:
# Runtime: 32 ms, faster than 80.60% of Python3 online submissions for Add Binary.
# Memory Usage: 14.4 MB, less than 22.51% of Python3 online submissions for Add Binary.
