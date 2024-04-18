class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def deleteNode(self, root, key: int):
        if root is None:
            return None
        if key < root.val:
            root.left = self.deleteNode(root.left, key)
        elif key > root.val:
            root.right = self.deleteNode(root.right, key)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            else:
                minimum_node = self.get_min_node(root.right)
                root.val = minimum_node.val
                root.right = self.deleteNode(root.right, root.val)
        return root
    
    def get_min_node(self, node):
        current = node
        while current and current.left:
            current = current.left
        return current
