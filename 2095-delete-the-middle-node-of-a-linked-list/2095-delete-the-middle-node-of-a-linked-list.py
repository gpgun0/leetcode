# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        
        if head.next == None:
            return None;
        
        h = head
        small = head
        fast = head
        
        while True:
            if fast.next.next == None:
                break
            
            fast = fast.next.next
            if fast.next == None:
                break
        
            small = small.next
    
        small.next = small.next.next
        return head