# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        def middle():
            slow, fast = head, head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            return slow
        mid = middle()

        def reverse():
            prev, curr = None, mid
            while curr:
                next_node = curr.next   # 1️⃣ save
                curr.next = prev        # 2️⃣ reverse link
                prev = curr             # 3️⃣ move prev forward
                curr = next_node        # move curr forward
            return prev  
        
        half1 = head
        half2 = reverse()
        while half2:
            if half1.val == half2.val:
                half1 = half1.next
                half2 = half2.next
            else:
                return False
        return True
