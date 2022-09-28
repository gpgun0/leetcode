# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        len_ = 1
        temp = head
        while temp.next:
            len_ += 1
            temp = temp.next
        
        if len_-n == 0:
            return head.next
            
        x = head
        for i in range(len_-n-1):
            x = x.next
        
        x.next = x.next.next
        return head