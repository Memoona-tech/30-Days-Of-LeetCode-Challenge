# SOLUTION 2
# ------------------ O(h) TC ----------- O(1) SC --------


class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
                        
        while root:
            if p.val > root.val and q.val > root.val:
                root = root.right
            elif p.val < root.val and q.val < root.val:
                root = root.left
            else:
                return root


# Q: why not TC is O(logn)
{
#    Short answer: we write the time as O(h) (where h = tree height) because that’s true for every BST.
#   If the BST is balanced then h = O(log n) and you can also say O(log n). But in the worst case a BST 
#  can be a straight chain (height h = n), so the only safe general bound is O(h) (which could be O(n) in the worst case).
}
