# Question: https://leetcode.com/problems/detect-capital/

# ------------------------------------------------------------------------------------------ #
# Solution 2: In-Built Python Libraries
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        return word.isupper() or word.islower() or word.istitle()
      
# Verdict:
# Runtime: 28 ms, faster than 91.10% of Python3 online submissions for Detect Capital.
# Memory Usage: 14.4 MB, less than 13.27% of Python3 online submissions for Detect Capital.
  
# ------------------------------------------------------------------------------------------ #
# Solution 1: Brute Force
class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        capitals, n = 0, len(word)
        for i in range(n):
            capitals += word[i].isupper()
        if (capitals == 0) or (capitals == n) or (capitals == 1 and word[0].isupper()):
            return True
        return False

# Verdict:
# Runtime: 50 ms, faster than 23.17% of Python3 online submissions for Detect Capital.
# Memory Usage: 14 MB, less than 91.67% of Python3 online submissions for Detect Capital.
# ------------------------------------------------------------------------------------------ #
