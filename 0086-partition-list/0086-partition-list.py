# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
        if not head:
            return head

        node = head
        sm_head = None
        sm_pointer = None
        lg_head = None
        lg_pointer = None

        while node:
            if sm_head and node.val < x:
                sm_pointer.next = node
                sm_pointer = sm_pointer.next
            elif lg_head and node.val >= x:
                lg_pointer.next = node
                lg_pointer = lg_pointer.next

            elif not sm_head and node.val < x:
                sm_pointer = node
                sm_head = ListNode()
                sm_head.next = sm_pointer
            elif not lg_head and node.val >= x:
                lg_pointer = node
                lg_head = ListNode()
                lg_head.next = lg_pointer
            
            node = node.next
        
        if lg_pointer:
            lg_pointer.next = None
        
        if sm_pointer and lg_head:
            sm_pointer.next = lg_head.next

        if sm_head:
            return sm_head.next
        
        return head