# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def detectCycle(self, head: Optional[ListNode]) -> Optional[ListNode]:
        slow, fast = head, head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if fast is slow: break
        else: 
            return None
        while head != slow:
             head, slow = head.next, slow.next
        return head 
