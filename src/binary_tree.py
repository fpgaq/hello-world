
class Node(object):
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

    @staticmethod
    def pre_order(root, nodes):
        if not root:
            return

        nodes.append(root.data)
        Node.pre_order(root.left, nodes)
        Node.pre_order(root.right, nodes)

    @staticmethod
    def in_order(root, nodes):
        if not root:
            return

        Node.in_order(root.left, nodes)
        nodes.append(root.data)
        Node.in_order(root.right, nodes)

    @staticmethod
    def post_order(root, nodes):
        if not root:
            return

        Node.post_order(root.left, nodes)
        Node.post_order(root.right, nodes)
        nodes.append(root.data)

    @staticmethod
    def level_traverse(root, nodes):
        if not root:
            return
        queue = [root]
        while queue:
            node = queue.pop(0)
            nodes.append(node.data)
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)



if __name__ == '__main__':
    nodes = [Node('A'), Node('B'), Node('C'), Node('D'), Node('E')]

    nodes[0].left = nodes[1]
    nodes[0].right = nodes[2]
    nodes[1].left = nodes[3]
    nodes[1].right = nodes[4]

    result = []
    Node.pre_order(nodes[0], result)
    print(result)
    result.clear()
    Node.in_order(nodes[0], result)
    print(result)
    result.clear()
    Node.level_traverse(nodes[0], result)
    print(result)

