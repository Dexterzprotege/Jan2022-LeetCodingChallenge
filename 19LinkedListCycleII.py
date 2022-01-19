# Question: https://leetcode.com/problems/linked-list-cycle-ii/

# Solution:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head is None or head.next is None:
            return None
        
        slow = fast = entry = head
        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next
            
            # Cycle is detected
            if slow == fast:
                while slow != entry: # Entry location is found
                    slow = slow.next
                    entry = entry.next
                return entry
        return None

# Verdict:
# Runtime: 73 ms, faster than 29.10% of Python3 online submissions for Linked List Cycle II.
# Memory Usage: 17.1 MB, less than 82.54% of Python3 online submissions for Linked List Cycle II.
