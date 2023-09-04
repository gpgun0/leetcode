# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        INF = int(1e9)
        
        while head:
            if head.val == INF:
                return True

            head.val = INF
            head = head.next
        
        return False