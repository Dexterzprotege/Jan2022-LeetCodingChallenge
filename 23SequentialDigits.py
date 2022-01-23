# Question: https://leetcode.com/problems/sequential-digits/

# ------------------------------------------------------------------------------------------------------- #
# Solution 3:
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        ans = []
        for i in range(1, 10):
            number = i
            nextNum = i
            while(number<=high and nextNum <10):
                if number>=low:
                    ans.append(number)
                nextNum += 1
                number = number*10+nextNum           
        return sorted(ans)

# Verdict:
# Runtime: 78 ms, faster than 5.95% of Python3 online submissions for Sequential Digits.
# Memory Usage: 14.3 MB, less than 53.17% of Python3 online submissions for Sequential Digits.

# ------------------------------------------------------------------------------------------------------- #
# Solution 2:
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        s = '123456789'
        ans = []
        for i in range(9):
            for j in range(i+1, 9):
                st = int(s[i: j+1])
                if st>=low and st<=high:
                    ans.append(st)
        return sorted(ans)
      
# Verdict:
# Runtime: 70 ms, faster than 5.95% of Python3 online submissions for Sequential Digits.
# Memory Usage: 14.3 MB, less than 53.17% of Python3 online submissions for Sequential Digits.

# ------------------------------------------------------------------------------------------------------- #
# Solution 1: Brute Force: Generate all and append
class Solution:
    def sequentialDigits(self, low: int, high: int) -> List[int]:
        digits = [12,23,34,45,56,67,78,89,
                123,234,345,456,567,678,789,
                1234,2345,3456,4567,5678,6789,                                                 
                12345,23456,34567,45678,56789,
                123456,234567,345678,456789,
                1234567,2345678,3456789,
                12345678,23456789,
                123456789]
        ans = []
        for i in range(len(digits)):
            if digits[i]>=low and digits[i]<=high:
                ans.append(digits[i])
            else:
                continue
        return ans

# Verdict:
# Runtime: 47 ms, faster than 21.83% of Python3 online submissions for Sequential Digits.
# Memory Usage: 14.4 MB, less than 22.22% of Python3 online submissions for Sequential Digits.
# ------------------------------------------------------------------------------------------------------- #
