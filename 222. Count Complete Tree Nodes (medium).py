# SOLUTION 1
# ------------------ O(log n) TC ----------- O(1) SC --------

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h
        def right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h
        
        lh = left_height(root)
        rh = right_height(root)

        if lh == rh:
            return (1 << lh) - 1   # (2 ** lh) - 1
        
        return 1 + self.countNodes(root.left) + self.countNodes(root.right)



# SOLUTION 2
# ------------------ O(log² n) TC ----------- O() SC --------

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        # Compute tree height
        h = 0
        node = root
        while node.left:
            h += 1
            node = node.left

        # Binary search on last level
        def exists(idx):
            node = root
            left, right = 0, (1 << h) - 1
            for _ in range(h):
                mid = (left + right) // 2
                if idx <= mid:
                    node = node.left
                    right = mid
                else:
                    node = node.right
                    left = mid + 1
            return node is not None

        left, right = 0, (1 << h) - 1
        while left <= right:
            mid = (left + right) // 2
            if exists(mid):
                left = mid + 1
            else:
                right = mid - 1

        return (1 << h) - 1 + left

# SOLUTION 3
# ------------------ O(n) TC ----------- O(h) SC --------

def countNodes(root):
    if not root:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)


# SOLUTION 4
# ------------------ O(n) TC ----------- O(1) SC --------

class Solution:
    def countNodes(self, root: Optional[TreeNode]) -> int:
        def left_height(node):
            h = 0
            while node:
                h += 1
                node = node.left
            return h

        def right_height(node):
            h = 0
            while node:
                h += 1
                node = node.right
            return h

        count = 0
        node = root

        while node:
            lh = left_height(node)
            rh = right_height(node)

            if lh == rh:
                # whole subtree is perfect
                count += (1 << lh) - 1
                break
            else:
                # root counts as 1
                count += 1

                # decide which side is perfect
                if left_height(node.left) == right_height(node.left):
                    # left subtree is perfect
                    count += (1 << left_height(node.left)) - 1
                    node = node.right
                else:
                    # right subtree is perfect
                    count += (1 << right_height(node.right)) - 1
                    node = node.left

        return count
