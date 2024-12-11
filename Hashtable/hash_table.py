class Hashtable:
  def __init__(self, size = 16):
    self.size = size
    self.hashmap = [[] for i in range(self.size)]

  def __str__(self):
    return str(self.__dict__)

  def _hash(self, key):
    hash = 0
    for i in range(len(key)):
      hash = (hash + ord(key[i]) * i) % self.size
      
    return hash

  def set(self, key, value):
    address = self._hash(key)

    # check if the buckets is empty
    if len(self.hashmap[address]) == 0:
      self.hashmap[address] = []
    else:
      # look for the key in the bucket to change the value
      for i in range(len(self.hashmap[address])):
        if self.hashmap[address][i][0] == key:
          self.hashmap[address][i][1] = value
          
          return self.hashmap

    # if bucket is empty and the key is new
    self.hashmap[address].append([key, value])

    return self.hashmap

  def get(self, key):
    address = self._hash(key)
    current_bucket = self.hashmap[address]
    
    # check if the bucket is empty
    if current_bucket != []:
      for i in range(len(current_bucket)):
        if current_bucket[i][0] == key:
            return current_bucket[i][1]
    
    return None

  def keys(self):
    keys = []

    for i in range(len(self.hashmap)):
      for j in range(len(self.hashmap[i])):
        keys.append(self.hashmap[i][j][0])

    return keys

  def list_items(self):
    items = []

    for i in range(len(self.hashmap)):
      for j in range(len(self.hashmap[i])):
        items.append(self.hashmap[i][j])

    return items
        

hash_table = Hashtable(2)
hash_table.set("fruits", "orange")
hash_table.set("vegetables", "cucumber")
hash_table.set("vegetables", "pepper") # It'll change the value from "cucumber" to "pepper"
hash_table.set("meats", "chicken")
print(hash_table.get("vegetables"))
print(hash_table.__str__())
print(hash_table.keys())
print(hash_table.list_items())


