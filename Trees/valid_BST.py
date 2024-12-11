def is_valid_BST(root):
    current_node = None
    queue = []
    queue.append(root)

    while len(queue) > 0:
        current_node = queue.pop(0)

        if current_node.left:
            queue.append(current_node.left)
        if current_node.right:
            queue.append(current_node.right)

        if current_node.right is not None and current_node.value > current_node.right.value:
            return False
        if current_node.left is not None and current_node.value < current_node.left.value:
            return False
        
    return True
        
        