class TreeNode:
    def __int__(self, val):
        self.val = val
        self.left = None
        self.right = None

class Solution:
    def isSameTree(self, p, q):
        if p is None and q is None:
            return True
        if p is None or q is None:
            return False
        if p.val != q.val:
            return False
        current_val = p.val == q.val
        left_sub_tree = self.isSameTree(p.left, q.left)
        right_sub_tree = self.isSameTree(p.right, q.right)

        return current_val and left_sub_tree and right_sub_tree

