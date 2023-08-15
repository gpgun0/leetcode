# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        node = head
        sm_head = sm_pointer = ListNode(0)
        lg_head = lg_pointer = ListNode(0)

        while node:
            if node.val < x:
                sm_pointer.next = node
                sm_pointer = sm_pointer.next
            elif node.val >= x:
                lg_pointer.next = node
                lg_pointer = lg_pointer.next
            
            node = node.next
        
        lg_pointer.next = None
        
        sm_pointer.next = lg_head.next

        return sm_head.next