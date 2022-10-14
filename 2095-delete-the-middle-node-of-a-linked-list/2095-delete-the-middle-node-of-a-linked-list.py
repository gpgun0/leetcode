# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def deleteMiddle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if head.next == None:
            return None;
        
        answer = small = fast = head
        
        while fast.next.next:
            fast = fast.next.next
            if fast.next == None:
                break
            
            small = small.next
            if fast.next.next == None:                
                break
            

        small.next = small.next.next
        return answer
