class TreeNode:
    def __init__(self, data):
        self.val = data
        self.left = None
        self.right = None


class Solution:
    def searchBST(self, root, val):
        if root is None:
            return None
        if root.val == val:
            return root
        if root.val > val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)


s = Solution()
root = TreeNode(4)
root.left = TreeNode(2)
root.right = TreeNode(7)

root.left.left = TreeNode(1)
root.left.right = TreeNode(3)

print(s.searchBST(root, 2))
print(s.searchBST(root, 0))
