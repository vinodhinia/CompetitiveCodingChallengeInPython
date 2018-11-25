class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class PostOrderTraversal:
    def __init__(self, root_node):
        self.root = root_node

    def post_order(self, root):
        if not root:
            return root
        self.post_order(root.left)
        self.post_order(root.right)
        print(root.data)

        #       4
        #      / \
        #     5   6
        #    /\   /\
        #   7  8 9  10
        # Left, Right, Root
        # Post Order : 7, 8, 5, 9, 10, 6, 4

    def post_order_with_stacks(self, root):
        stack1 = []
        stack2 = []


        # 1 -> [4], 2 -> []
        # 1 -> [5, 6], 2 -> [4]
        # 1 -> [5], 2 -> [4, 6] -> 1 -> [5,9 , 10] 2->[4, 6]
        # 1 -> [5,9 , 10] 2->[4, 6]  => 2  [4,6, 10, 9]
        # 1 -> [5,9 , 10] 2->[4, 6]  =>  [4,6, 10, 9]
        pass


if __name__ == '__main__':
    root_node = TreeNode(4)
    root_node.left = TreeNode(5)
    root_node.right = TreeNode(6)

    root_node.left.left = TreeNode(7)
    root_node.left.right = TreeNode(8)

    root_node.right.left = TreeNode(9)
    root_node.right.right = TreeNode(10)
    traversal = PostOrderTraversal(root_node)
    traversal.post_order(root_node)
