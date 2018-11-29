class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None

class Solution:
    def isSymmertic(self, root):
        if root is None:
            return True
        return self.isSymmetricHelper(root.left, root.right)

    def isSymmetricHelper(self, root1, root2):
        if root1 is None and root2 is None:
            return True
        if root1 is None or root2 is None:
            return False
        if root1.val != root2.val:
            return False
        current_val = root1.val == root2.val
        return current_val and self.isSymmetricHelper(root1.left, root2.right) and self.isSymmetricHelper(root1.right, root2.left)


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)

root.left.left = TreeNode(3)
root.left.right = TreeNode(4)

root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

s = Solution()
print(s.isSymmertic(root))


