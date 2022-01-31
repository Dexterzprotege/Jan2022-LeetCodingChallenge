# Question: https://leetcode.com/problems/richest-customer-wealth/

# Solution:
class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        ans = 0
        for account in accounts:
            ans = max(ans, sum(account))
        return ans
      
# Verdict:
# Runtime: 89 ms, faster than 21.84% of Python3 online submissions for Richest Customer Wealth.
# Memory Usage: 13.9 MB, less than 99.25% of Python3 online submissions for Richest Customer Wealth.
