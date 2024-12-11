def traverse_inorder(node, result):
  if node.left is not None:
    traverse_inorder(node.left, result)

  result.append(node.value)

  if node.right is not None:
    traverse_inorder(node.right, result)

  return result

def traverse_preorder(node, result):
  result.append(node.value)

  if node.left is not None:
    traverse_preorder(node.left, result)
  
  if node.right is not None:
    traverse_preorder(node.right, result)

  return result

def traverse_postorder(node, result):
  if node.left is not None:
    traverse_postorder(node.left, result)

  if node.right is not None:
    traverse_postorder(node.right, result)

  result.append(node.value)

  return result

#     9
#  4     20
#1  6  15  170
