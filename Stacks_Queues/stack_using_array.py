class Stack:
  def __init__(self):
    self.stack = []
    self.length = 0

  def peek(self):
    if self.length == 0:
      return "stack is empty"

    else:
      return self.stack[self.length - 1]

  def push(self, value):
    self.stack.append(value) # O(n) if the stack's capacity is full, otherwise O(1)
    self.length += 1

    return self.stack

  def pop(self):
    if self.length == 0:
      return "stack is empty"
    else:
      popped_item = self.stack[self.length - 1]
      del self.stack[self.length - 1]
      self.length -= 1

      return popped_item


my_stack = Stack()
my_stack.push("google")
my_stack.push("facebook")
my_stack.push("discord")

print(my_stack.peek())
print(my_stack.stack)

my_stack.pop()
my_stack.pop()
my_stack.pop()

print(my_stack.peek())
print(my_stack.stack)