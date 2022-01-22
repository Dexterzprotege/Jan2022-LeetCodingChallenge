# Question: https://leetcode.com/problems/stone-game-iv/

# Soltuion:
class Solution:
    def winnerSquareGame(self, n: int) -> bool:
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
TLE
