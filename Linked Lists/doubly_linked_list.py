class Node:
  def __init__(self, value, next = None, prev = None):
    self.value = value
    self.next = next
    self.prev = prev

class DoublyLinkedList:
  def __init__(self, value):
    self.head = Node(value)
    self.tail = self.head
    
    self.length = 1

  def display(self):
    current_node = self.head
    linked_list_str = ""

    while current_node.next is not None:
      linked_list_str += str(current_node.value) + " -> "
      current_node = current_node.next

    linked_list_str += str(current_node.value)
      
    return linked_list_str

  def reverse(self):
    current_node = self.tail
    linked_list_str = ""

    while current_node.prev is not None:
      linked_list_str += str(current_node.value) + " -> "
      current_node = current_node.prev

    linked_list_str += str(current_node.value)

    return linked_list_str

  def append(self, value):

    if self.head is None:
      return "this isn't a linked list"

    new_node = Node(value=value, prev=self.tail)

    new_node.prev = self.tail
    self.tail.next = new_node
    self.tail = new_node
    
    self.length += 1

    return self

  def prepend(self, value):

    if self.head is None:
      return "this isn't a linked list"
      
    new_node = Node(value=value, next=self.head)
    
    self.head.prev = new_node
    self.head = new_node

    self.length += 1

    return self

  def traverse_to_index(self, index):
    count = 0
    current_node = self.head
    
    while count < index:
      current_node = current_node.next
      count += 1

    return current_node

  def insert(self, index, value):

    if self.head is None:
      return "this isn't a linked list"
    elif index == 0:
      self.prepend(value)
      return self
    elif index >= self.length:
      self.append(value)
      return self
    else:

      # node that comes before the new one
      leader = self.traverse_to_index(index - 1)
  
      follower = leader.next
      new_node = Node(value, follower, leader)
      leader.next = new_node
      follower.prev = new_node
  
      self.length += 1

      return self
      

  def delete(self, index):

    if self.head is None:
      return "this isn't a linked list"
    elif index >= self.length - 1:
      return "the index exceeds the length"
    elif index == 0:
      self.head = self.head.next
      
      self.head.prev = None
      return self
    else:

      leader = self.traverse_to_index(index - 1)
  
      unwanted_node = leader.next

      # check if the unwanted node is the tail
      if unwanted_node == self.tail:
        leader.next = None
        self.tail = leader
      else:
        follower = unwanted_node.next
        leader.next = follower
        
        follower.prev = leader
        

      self.length -= 1

    return self

linked_list = DoublyLinkedList(2)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(1)
linked_list.append(4)
linked_list.prepend(0)

print(linked_list.head.value)
print(linked_list.tail.value)
print(linked_list.display())
print(linked_list.reverse())

linked_list.insert(2, 10)
linked_list.insert(0, 15)
linked_list.insert(8, 20)
linked_list.insert(9, 25)

print(linked_list.tail.value)
print(linked_list.display())

linked_list.insert(0, 43)
linked_list.delete(2)
linked_list.delete(0)


print(linked_list.tail.value)
print(linked_list.display())

print(linked_list.delete(8))

print(linked_list.tail.value)
print(linked_list.display())


linked_list.delete(8)
linked_list.insert(20,30)

print(linked_list.tail.value)
print(linked_list.display())
print(linked_list.reverse())


