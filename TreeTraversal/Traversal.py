class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class Traversal:
    def __init__(self, root):
        self.root  = root

    def pre_order_traversal(self, root):
        if not root:
            return root
        print(root.data)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)


        #       4
        #      / \
        #     5   6
        #    /\   /\
        #   7  8 9  10
        # Pre Order : 4, 5, 7, 8, 6, 9, 10
if __name__ == '__main__':

    root_node = TreeNode(4)
    root_node.left = TreeNode(5)
    root_node.right = TreeNode(6)


    root_node.left.left = TreeNode(7)
    root_node.left.right = TreeNode(8)

    root_node.right.left = TreeNode(9)
    root_node.right.right = TreeNode(10)

    traverse = Traversal(root_node)
    traverse.pre_order_traversal(root_node)


