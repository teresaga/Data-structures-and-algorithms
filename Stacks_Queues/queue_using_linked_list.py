class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

class Queue:
  def __init__(self):
    self.first = None
    self.last = None
    self.length = 0

  def display(self):
    current_node = self.first
    queue = ""

    while current_node is not None:
      queue += str(current_node.value) + "->"
      current_node = current_node.next

    queue += "None"

    return queue

  def peek(self):
    if self.first is None:
      return None
    else:
      return self.first.value

  def enqueue(self, value):
    new_node = Node(value)
    
    if self.first is None: # Queue is empty
      self.first = new_node
      self.last = new_node
    else:
      self.last.next = new_node
      self.last = new_node

    self.length += 1

    return self

  def dequeue(self):
    dequeued_item = self.last

    if self.first is None:  # Queue is empty
      return None
    elif self.first is self.last:
      self.last = None

    else:
      self.first = self.first.next
    
    self.length -= 1

    return dequeued_item.value


my_queue = Queue()
my_queue.enqueue("Joy")
my_queue.enqueue("Matt")
my_queue.enqueue("Pavel")
my_queue.enqueue("Samir")

print(my_queue.peek())
print(my_queue.display())

my_queue.dequeue()
my_queue.dequeue()
my_queue.dequeue()

print(my_queue.peek())
print(my_queue.display())