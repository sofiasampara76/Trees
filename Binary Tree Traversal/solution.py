# Pre-order traversal
def pre_order(node):
    def order(node):
        if node.left:
            pre_order_list.append(node.left.data)
            order(node.left)
        if node.right:
            pre_order_list.append(node.right.data)
            order(node.right)
    pre_order_list = []
    if node:
        pre_order_list = [node.data]
        order(node)
    return pre_order_list

def post_order(node):
    def order(node):
        if node.left:
            order(node.left)
            post_order_list.append(node.left.data)
        if node.right:
            order(node.right)
            post_order_list.append(node.right.data)
    post_order_list = []
    if node:
        order(node)
        post_order_list.append(node.data)
    return post_order_list

def in_order(node):
    in_order_list = []
    def order(node):
        if node.left:
            order(node.left)
        in_order_list.append(node.data)
        if node.right:
            order(node.right)
    if node:
        order(node)
    return in_order_list
