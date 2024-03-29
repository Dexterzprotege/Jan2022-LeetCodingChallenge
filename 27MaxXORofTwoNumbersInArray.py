# Question: https://leetcode.com/problems/maximum-xor-of-two-numbers-in-an-array/

# Solution: Masking the Max possible value
class Solution:
    def findMaximumXOR(self, nums: List[int]) -> int:
        ans, mask = 0, 0
        # The maxResult is a record of the largest XOR we got so far. if it's 11100 at i = 2, it means 
        # before we reach the last two bits, 11100 is the biggest XOR we have, and we're going to explore
        # whether we can get another two '1's and put them into maxResult
        
        # This is a greedy part, since we're looking for the largest XOR, we start 
        # from the very begining, aka, the 31st postition of bits. 
        for i in range(31, -1, -1):
            # The mask will grow like  100..000 , 110..000, 111..000,  then 1111...111
            # for each iteration, we only care about the left parts
            mask = mask | (1 << i)
            setlist = set()
            for num in nums:
                # we only care about the left parts, for example, if i = 2, then we have
                # {1100, 1000, 0100, 0000} from {1110, 1011, 0111, 0010}
                setlist.add(mask & num)
                
            # if i = 1 and before this iteration, the maxResult we have now is 1100, 
            # my wish is the maxResult will grow to 1110, so I will try to find a candidate
            # which can give me the greedyTry;
            temp = ans | (1 << i)
            for prefix in setlist:
                # This is the most tricky part, coming from a fact that if a ^ b = c, then a ^ c = b;
                # now we have the 'c', which is greedyTry, and we have the 'a', which is leftPartOfNum
                # If we hope the formula a ^ b = c to be valid, then we need the b, 
                # and to get b, we need a ^ c, if a ^ c exisited in our set, then we're good to go
                if temp ^ prefix in setlist:
                    ans = temp
                    break
            # If unfortunately, we didn't get the greedyTry, we still have our max, 
            # So after this iteration, the max will stay at 1100.
        return ans

# Verdict:
# Runtime: 2534 ms, faster than 58.96% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
# Memory Usage: 33.5 MB, less than 97.65% of Python3 online submissions for Maximum XOR of Two Numbers in an Array.
