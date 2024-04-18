from collections import deque

def tree_by_levels(node):
    queue = deque()
    levels = []
    if node:
        queue.append(node)
        levels.append(node.value)
    while queue:
        popped = queue.popleft()
        if popped.left:
            levels.append(popped.left.value)
            queue.append(popped.left)
        if popped.right:
            queue.append(popped.right)
            levels.append(popped.right.value)
    return levels
