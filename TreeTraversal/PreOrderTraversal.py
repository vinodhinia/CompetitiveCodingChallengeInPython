class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

class PreOrderTraversal:
    def __init__(self, root):
        self.root = root

    def pre_order_traversal(self, root):
        if not root:
            return root
        print(root.data)
        self.pre_order_traversal(root.left)
        self.pre_order_traversal(root.right)

    def pre_order_traversal_iterative(self, root):
        stack = []
        stack.append(root)
        while len(stack) != 0:
            node = stack.pop()
            print(node.data)
            if node.right != None:
                stack.append(node.right)
            if node.left != None:
                stack.append(node.left)



        #       4
        #      / \
        #     5   6
        #    /\   /\
        #   7  8 9  10
        # Pre Order : 4, 5, 7, 8, 6, 9, 10

if __name__ == '__main__':
    #Initialize the Tree
    root_node = TreeNode(4)
    root_node.left = TreeNode(5)
    root_node.right = TreeNode(6)


    root_node.left.left = TreeNode(7)
    root_node.left.right = TreeNode(8)

    root_node.right.left = TreeNode(9)
    root_node.right.right = TreeNode(10)

    traverse = PreOrderTraversal(root_node)
    traverse.pre_order_traversal(root_node)

    print('Iterative way of traversing the tree')

    traverse.pre_order_traversal_iterative(root_node)




