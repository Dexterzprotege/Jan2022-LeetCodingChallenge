# Question: https://leetcode.com/problems/robot-bounded-in-circle/

# Solution:
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        curr_pos = [0, 0]
        curr_dir = 0 # North
        
        directions = {
            0: [0, 1],  # North
            1: [1, 0],  # East
            2: [0, -1], # West
            3: [-1, 0]  # South
        }
        
        for i in instructions:
            if i == "L":
                curr_dir = (curr_dir - 1) % 4
            elif i == "R":
                curr_dir = (curr_dir + 1) % 4
            else: # G
                curr_pos[0] += directions[curr_dir][0]
                curr_pos[1] += directions[curr_dir][1]
                
        if curr_pos  == [0, 0]: # Position never changed, or back to the same position
            return True
        if curr_dir != 0: # Not facing North, hence it will eventually create a circle
            return True
        return False
        

# Verdict:
# Runtime: 28 ms, faster than 85.98% of Python3 online submissions for Robot Bounded In Circle.
# Memory Usage: 14.3 MB, less than 15.52% of Python3 online submissions for Robot Bounded In Circle.
