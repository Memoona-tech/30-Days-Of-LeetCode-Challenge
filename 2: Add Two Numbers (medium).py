# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class Solution:

    # ---------------------------------------------------
    # ✅ Solution 1: Digit-by-digit (best for LeetCode 2)
    # Idea:
    #   - Traverse both lists from head (since digits are already reversed).
    #   - Add corresponding digits + carry.
    #   - Build result list as we go.
    #
    # Time Complexity: O(max(n, m))  (we process each digit once)
    # Space Complexity: O(max(n, m)) (for the output linked list)
    # ---------------------------------------------------
    def addTwoNumbers_digitwise(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            total = v1 + v2 + carry
            carry = total // 10
            curr.next = ListNode(total % 10)
            curr = curr.next
            if l1: l1 = l1.next
            if l2: l2 = l2.next
        return dummy.next


    # ---------------------------------------------------
    # ✅ Solution 2: Reverse + Integer + String (your approach)
    # Idea:
    #   - Reverse both lists to get normal order.
    #   - Convert lists into integers.
    #   - Add integers and convert result back into linked list.
    #   - Reverse final linked list to restore reverse order.
    #
    # Time Complexity: O(n + m)  (reversals + traversals + conversions)
    # Space Complexity: O(n + m) (string to store the result + output list)
    # ---------------------------------------------------
    def addTwoNumbers_stringy(self, l1: ListNode, l2: ListNode) -> ListNode:
        def revL(head):
            prev, curr = None, head
            while curr:
                nxt = curr.next
                curr.next = prev
                prev = curr
                curr = nxt
            return prev

        def listVal(node):
            num = 0
            while node:
                num = num * 10 + node.val
                node = node.next
            return num

        def toLL(s):
            dummy = node = ListNode()
            for ch in s:
                node.next = ListNode(int(ch))
                node = node.next
            return dummy.next

        l1 = revL(l1)
        l2 = revL(l2)
        res = str(listVal(l1) + listVal(l2))
        return revL(toLL(res))


    # ---------------------------------------------------
    # ✅ Solution 3: Stack-based (useful for LeetCode 445, forward order)
    # Idea:
    #   - Push digits of both lists onto stacks.
    #   - Pop from stacks while adding with carry.
    #   - Build the result list backwards.
    #
    # Time Complexity: O(n + m)  (each digit pushed & popped once)
    # Space Complexity: O(n + m) (stacks + output linked list)
    # ---------------------------------------------------
    def addTwoNumbers_stacks(self, l1: ListNode, l2: ListNode) -> ListNode:
        s1, s2 = [], []
        while l1:
            s1.append(l1.val)
            l1 = l1.next
        while l2:
            s2.append(l2.val)
            l2 = l2.next

        carry = 0
        head = None
        while s1 or s2 or carry:
            a = s1.pop() if s1 else 0
            b = s2.pop() if s2 else 0
            total = a + b + carry
            node = ListNode(total % 10)
            node.next = head
            head = node
            carry = total // 10
        return head
