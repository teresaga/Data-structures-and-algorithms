class Node:
  def __init__(self, value, next = None):
    self.value = value
    self.next = next

class Stack:
  def __init__(self):
    self.top = None
    self.bottom = None
    self.length = 0

  def display(self):
    current_node = self.top
    stack = ""

    while current_node is not None:
      stack += str(current_node.value) + "->"
      current_node = current_node.next

    stack += "None"

    return stack

  def peek(self):
    if self.top is None: # stack empty
      return "stack is empty"
    else:

      return self.top.value

  def push(self, value):
    new_node = Node(value)

    if self.top is None: # stack empty
      self.top = new_node
      self.bottom = new_node

    else:
      holding_point = self.top
      self.top = new_node
      self.top.next = holding_point

    self.length += 1

    return value

  def pop(self):
    if self.top is None: # stack empty
      return None

    elif self.top is self.bottom:
      self.bottom = None
    else:
      self.top = self.top.next
      self.length -= 1

      return self


my_stack = Stack()
my_stack.push("google")
my_stack.push("facebook")
my_stack.push("discord")

print(my_stack.peek())
print(my_stack.display())

my_stack.pop()
my_stack.pop()


print(my_stack.peek())
print(my_stack.display())

my_stack.pop()

print(my_stack.peek())
print(my_stack.display())