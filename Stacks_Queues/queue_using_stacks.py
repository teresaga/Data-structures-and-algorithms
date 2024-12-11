class Queue:
  def __init__(self):
    self.stack1 = []
    self.stack2 = []
    self.length = 0
    
  def enqueue(self, value):
    for i in range(len(self.stack2)):
      self.stack1.append(self.stack2.pop())

    self.stack1.append(value)
    self.length += 1
    
    return None

  def dequeue(self):
    if not self.stack1 and not self.stack2:
      return "Queue is empty"

    for i in range(len(self.stack1)):
      self.stack2.append(self.stack1.pop())

    self.length -= 1
    
    return self.stack2.pop()


  def peek(self):
    if not self.stack1 and not self.stack2:
      return "Queue is empty"
    elif not self.stack2:
      return self.stack1[0]
    else:
      return self.stack2[len(self.stack2)-1]


  def empty(self):
    if self.length == 0:
      return True
    return False

my_queue = Queue()
print(my_queue.peek())
my_queue.enqueue('Joy')
my_queue.enqueue('Matt')
my_queue.enqueue('Pavel')

print(my_queue.__dict__)
print(my_queue.peek())

print(my_queue.dequeue())
print(my_queue.__dict__)
print(my_queue.dequeue())
print(my_queue.dequeue())

print(my_queue.peek())

print(my_queue.__dict__)
