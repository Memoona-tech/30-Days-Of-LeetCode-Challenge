# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if (not head) or (not head.next) or k==0:
            return head

        n = 1
        curr, end = head, head

        while curr.next:
            curr = curr.next
            n += 1
        end = curr
        k = k%n
        if k == 0:
            return head
        p = n - k - 1
        point = head

        for i in range(p):
            point = point.next
        
        new_h = point.next
        point.next = None
        end.next = head

        return new_h


# A little Clean

class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:

        # Edge cases
        if not head or not head.next or k == 0:
            return head

        # 1️⃣ Find length and tail
        length = 1
        curr = head
        while curr.next:
            curr = curr.next
            length += 1
        tail = curr

        # 2️⃣ Reduce k
        k %= length
        if k == 0:
            return head

        # 3️⃣ Find breaking point
        steps = length - k - 1
        point = head
        for _ in range(steps):
            point = point.next

        # 4️⃣ Rewire list
        new_head = point.next
        point.next = None
        tail.next = head

        return new_head

