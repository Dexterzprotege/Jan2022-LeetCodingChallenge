# Question: https://leetcode.com/problems/stone-game-iv/

# ----------------------------------------------------------------------------------------- #

# Solution 3:
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [0]*100001
        @lru_cache(None)
        def helper(n):
            if n <= 0:
                return False
            if dp[n] != 0:
                return dp[n]
            for i in range(0, n+1):
                if dp[i]:
                    continue
                k = 1
                while i + k * k <= n:
                    dp[i+k*k] = True
                    k += 1
            return dp[n]
        return helper(n)    
    
# Verdict:
# Runtime: 272 ms, faster than 86.83% of Python3 online submissions for Stone Game IV.
# Memory Usage: 15 MB, less than 59.88% of Python3 online submissions for Stone Game IV.

# ----------------------------------------------------------------------------------------- #

# Solution 2:
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        dp = [-1]*100001
        def helper(n):
            if n <= 0:
                return 0
            if dp[n] != -1:
                return dp[n]
            i = 1
            while i*i <= n:
                if helper(n-i*i) == 0:
                    dp[n] = 1
                    return 1
                i += 1
            return 0
        return helper(n)    

# Verdict:
# Runtime: 4027 ms, faster than 18.56% of Python3 online submissions for Stone Game IV.
# Memory Usage: 164.2 MB, less than 9.58% of Python3 online submissions for Stone Game IV.

# ----------------------------------------------------------------------------------------- #

# Soltuion 1:
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
        @lru_cache(None)
        def helper(n):
            if n <= 0:
                return 0
            i = 1
            while i*i <= n:
                if helper(n-i*i) == 0:
                    return 1
                i += 1
            return 0
        return helper(n)

# Verdict:
# Runtime: 4595 ms, faster than 16.77% of Python3 online submissions for Stone Game IV.
# Memory Usage: 161 MB, less than 9.58% of Python3 online submissions for Stone Game IV.

# ----------------------------------------------------------------------------------------- #
