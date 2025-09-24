# SOLUTION 1
# ------------------ O(n) TC ----------- O(1) SC --------

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:

        dummy = res = ListNode(0, head)

        for _ in range(n):
            head = head.next
        
        while head:
            head = head.next
            dummy = dummy.next
        
        dummy.next = dummy.next.next

        return res.next

# Solution 2

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # create a dummy node before head (helps when deleting head itself)
        dummy = ListNode(0, head)

        # two pointers
        first = dummy
        second = dummy

        # move first n+1 steps ahead
        for _ in range(n + 1):
            first = first.next

        # move both until first reaches end
        while first:
            first = first.next
            second = second.next

        # second is just before the node to delete
        second.next = second.next.next

        return dummy.next

# SOLUTION 3
# ------------------ O(n) TC ----------- O(n) SC --------

def removeNthFromEnd(self, head, n):
    dummy = ListNode(0, head)
    stack = []
    curr = dummy

    # push all nodes
    while curr:
        stack.append(curr)
        curr = curr.next

    # pop n nodes
    for _ in range(n):
        stack.pop()

    # now top is the node before target
    prev = stack[-1]
    prev.next = prev.next.next
    return dummy.next

# SOLUTION 4
# ------------------ O(n) TC ----------- O(n) SC --------

class Solution:
    def removeNthFromEnd(self, head, n):
        def helper(node):
            if not node:
                return 0, node
            count, nxt = helper(node.next)
            count += 1
            if count == n:
                return count, nxt   # skip this node
            node.next = nxt
            return count, node
        _, new_head = helper(head)
        return new_head

