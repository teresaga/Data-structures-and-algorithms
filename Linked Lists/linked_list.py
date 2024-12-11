class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

class LinkedList:
  def __init__(self, value):
    self.head = Node(value)
    self.tail = self.head

    self.length = 1

  def display(self):
    current_node = self.head
    linked_list_str = ""

    while current_node is not None:
      linked_list_str += str(current_node.value) + " -> "
      current_node = current_node.next

    linked_list_str += "None"

    return linked_list_str

  def append(self, value):

    if self.head is None:
      return "this isn't a linked list"

    new_node = Node(value)
    self.tail.next = new_node
    self.tail = new_node

    self.length += 1

    return self

  def prepend(self, value):

    if self.head is None:
      return "this isn't a linked list"

    new_node = Node(value, self.head)
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

      aux = leader.next
      new_node = Node(value, aux)
      leader.next = new_node

      self.length += 1

      return self


  def delete(self, index):

    if self.head is None:
      return "this isn't a linked list"
    elif index >= self.length - 1:
      return "the index exceeds the length"
    elif index == 0:
      self.head = self.head.next
      return self
    else:

      leader = self.traverse_to_index(index - 1)

      unwanted_node = leader.next

      # check if the unwanted node is the tail
      if unwanted_node == self.tail:
        leader.next = None
        self.tail = leader
      else:
        leader.next = unwanted_node.next


      self.length -= 1

    return self

  def reverse(self): #reverse with a space complexity of O(n)
    if self.length <= 0:
      return "Linked list is empty"
    elif self.length == 1:
      return [self.head.value]
    else:
      reversed_list = LinkedList(self.head.value)
      current_node = self.head

      while current_node.next is not None:
        current_node = current_node.next
        reversed_list.prepend(current_node.value)

      return reversed_list

  def reverse2(self):
    if self.length == 1:
      return self.head
    else:
      first = self.head
      second = first.next

      while second is not None:
        temp = second.next # save the next of second (third)

        # change item first and second
        second.next = first
        first = second

        # move second to the next value (third)
        second = temp

      self.head.next = None
      self.head = first

      return self
      

linked_list = LinkedList(2)
linked_list.append(2)
linked_list.append(3)
linked_list.prepend(1)
linked_list.append(4)
linked_list.prepend(0)

print(linked_list.tail.value)
print(linked_list.display())

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
print(linked_list.reverse().display())

