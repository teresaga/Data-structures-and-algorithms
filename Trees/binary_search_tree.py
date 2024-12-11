from traversal import traverse_inorder, traverse_postorder, traverse_preorder
from valid_BST import is_valid_BST

class Node:
  def __init__(self, value):
    self.value = value
    self.left = None
    self.right = None

class BinarySearchTree:
  def __init__(self):
    self.root = None

  def insert(self, value):
    if self.root is None:
      self.root = Node(value)
      return "added successfully"

    else:
      # start traverse from root
      current_node = self.root
      
      while True:
        if current_node.value > value: # left subtree
          if current_node.left is None:
            current_node.left = Node(value)
            break
          current_node = current_node.left
          
        else: # current_node.value <= value: right subtree
          if current_node.right is None:
            current_node.right = Node(value)
            break
          current_node = current_node.right
  
      return "added successfully"
      

  def lookup(self, value):
    if self.root is None:
      return None
    else:

      # start traverse from root
      current_node = self.root

      while current_node is not None:
        if current_node.value > value:
          current_node = current_node.left
        elif current_node.value < value:
          current_node = current_node.right
        elif current_node.value == value:
          return current_node.value

      return None
            

  def remove(self, value):
    ## empty tree
    if self.root is None:
      return "Tree is empty"
    else:
      #@ Search node with value
      current_node = self.root
      parent_node = None

      while current_node is not None:
        if current_node.value > value:
          parent_node = current_node
          current_node = current_node.left
        elif current_node.value < value:
          parent_node = current_node
          current_node = current_node.right
        elif current_node.value == value:
          #############        Everything starts here!      ##################
              
          ## Option 1: no right child
          if current_node.right is None:
            if self.root is current_node: #target is the root
              self.root = current_node.left
            elif parent_node.left is current_node: # / left
              parent_node.left = current_node.left
            elif parent_node.right is current_node: # / right
              parent_node.right = current_node.left
          
          ## Option 2: right child doesn't have a left child
          elif current_node.right.left is None:
              current_node.right.left = current_node.left
              if self.root is current_node: #target is the root
                self.root = current_node.right
              else:
      
                # modify address of target's parent
                if parent_node.left is current_node: # / left: target is the left child of parent
                  parent_node.left = current_node.right
                elif parent_node.right is current_node: # / right
                  parent_node.right = current_node.right
    
          ## Option 3: right child has a left child
          else:
            #@ Find the child on the far left
            leftmost_node = current_node.right.left
            leftmost_parent_node = None
    
            while leftmost_node is not None:
              leftmost_parent_node = leftmost_node
              leftmost_node = leftmost_node.left
    
            # lestmost parent's left subtree is now lestmost's right subtree
            leftmost_parent_node.left = leftmost_node.right
            # lestmost node update its children
            leftmost_node.left = current_node.left
            leftmost_node.right = current_node.right
            
            # modify address of target's parent
            if self.root is current_node:  # / target is the root
              self.root = leftmost_node
            elif parent_node.left is current_node: #left child of its parent
              parent_node.left = leftmost_node
            elif parent_node.right is current_node: #right child of its parent
              parent_node.right = leftmost_node

          return "removed successfully"

  def breadth_first_search(self):
    queue = []
    result = []

    current_node = None
    # begin traversal
    queue.append(self.root)

    while len(queue) > 0: # while queue is not empty
      current_node = queue.pop(0)
      result.append(current_node.value)

      if current_node.left is not None:
        queue.append(current_node.left)
      if current_node.right is not None:
        queue.append(current_node.right)

    return result
  
  def breadth_first_search_recursive(self, queue, result):
    if len(queue) == 0:
      return result
    
    current_node = queue.pop(0)
    result.append(current_node.value)

    if current_node.left is not None:
      queue.append(current_node.left)
    if current_node.right is not None:
      queue.append(current_node.right)

    return self.breadth_first_search_recursive(queue, result)

  def DFS_inorder(self):
    return traverse_inorder(self.root, [])
  
  def DFS_preorder(self):
    return traverse_preorder(self.root, [])
  
  def DFS_postorder(self):
    return traverse_postorder(self.root, [])
  

def traverse(node):
  tree = Node(node.value)
  tree.left = None if node.left is None else traverse(node.left)
  tree.right = None if node.right is None else traverse(node.right)
  return (str(tree.__dict__)).replace('\'',"")

tree = BinarySearchTree()
#tree.insert(7)

tree.insert(9)

#tree.insert(8)

tree.insert(4)
tree.insert(6)
tree.insert(20)
tree.insert(170)
tree.insert(15)
tree.insert(1)

#print(tree.remove(20))
#print(tree.lookup(170))
#print(traverse(tree.root))

##### BFS
#print(tree.breadth_first_search())
#print(tree.breadth_first_search_recursive([tree.root], []))

##### DFS
print(tree.DFS_inorder())
print(tree.DFS_preorder())
print(tree.DFS_postorder())

### IS VALID BST?
print(is_valid_BST(tree.root))

#JSON.stringify(traverse(tree.root));
#console.log(tree.lookup(20));
#     9
#  4     20
#1  6  15  170

"""
function traverse(node) {
  const tree = { value: node.value };
  tree.left = node.left === null ? null : traverse(node.left);
  tree.right = node.right === null ? null : traverse(node.right);
  return tree;
}
"""