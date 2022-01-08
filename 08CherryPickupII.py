# Question: https://leetcode.com/problems/cherry-pickup-ii/

# Solution:
class Solution:
    def cherryPickup(self, grid: List[List[int]]) -> int:
        @lru_cache(None)
        def dfs(row, col1, col2, n, m):
            if row == n:
                return 0
            cherries = grid[row][col1] if col1 == col2 else grid[row][col1] + grid[row][col2]
            ans = 0
            
            for nc1 in range(col1-1 , col1+2):
                for nc2 in range(col2-1, col2+2):
                    if m > nc1 >= 0 and m > nc2 >= 0:
                        ans = max(ans, dfs(row+1, nc1, nc2, n, m))
            return ans + cherries
                    
        n, m = len(grid), len(grid[0])
        return dfs(0, 0, m-1, n, m)

# Verdict:
# Runtime: 1144 ms, faster than 69.80% of Python3 online submissions for Cherry Pickup II.
# Memory Usage: 45.3 MB, less than 5.49% of Python3 online submissions for Cherry Pickup II.
