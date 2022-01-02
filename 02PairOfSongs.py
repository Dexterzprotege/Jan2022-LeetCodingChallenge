# Question: https://leetcode.com/problems/pairs-of-songs-with-total-durations-divisible-by-60/

# Solution:
class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        ans = 0
        dp = [0] * 61
        for i in time:
            mod = i % 60
            ans += dp[60 - mod]
            dp[mod if mod else 60] += 1
        return ans

# Verdict:
# Runtime: 350 ms, faster than 12.11% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
# Memory Usage: 17.9 MB, less than 48.64% of Python3 online submissions for Pairs of Songs With Total Durations Divisible by 60.
