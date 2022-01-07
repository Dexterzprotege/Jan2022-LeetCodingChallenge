# Question: https://leetcode.com/problems/linked-list-random-node/

# Solution2: Reservoir Sampling:
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import random
    
    def __init__(self, head: Optional[ListNode]):
        self.head = head

    def getRandom(self) -> int:
        curr = self.head
        i = 1
        res = 0
        while curr:
            if random.random() < 1 / i:
                res = curr.val
            curr = curr.next
            i += 1
        return res

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# Verdict:
# Runtime: 149 ms, faster than 28.87% of Python3 online submissions for Linked List Random Node.
# Memory Usage: 17.4 MB, less than 56.84% of Python3 online submissions for Linked List Random Node.


# Solution1: Math.random of a list
# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    import random
    
    def __init__(self, head: Optional[ListNode]):
        self.arr = []
        while head:
            self.arr.append(head.val)
            head = head.next

    def getRandom(self) -> int:
        return random.choice(self.arr)

# Your Solution object will be instantiated and called as such:
# obj = Solution(head)
# param_1 = obj.getRandom()

# Verdict:
# Runtime: 129 ms, faster than 32.52% of Python3 online submissions for Linked List Random Node.
# Memory Usage: 17.3 MB, less than 85.41% of Python3 online submissions for Linked List Random Node.
