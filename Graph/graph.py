class Graph:
  def __init__(self):
    self.number_nodes = 0
    self.adjacent_list = {}

  def add_vertex(self, node):
    self.adjacent_list[node] = []
    self.number_nodes += 1
    return "added successfully"

  def add_edge(self, node1, node2):
    if node1 not in self.adjacent_list.keys():
      return "node1 doesn't exist"
    elif node2 not in self.adjacent_list.keys():
      return "node2 doesn't exist"
    else:
      self.adjacent_list[node1].append(node2)
      self.adjacent_list[node2].append(node1)
      return "added successfully"

  def show_connections(self):
    all_nodes = self.adjacent_list.keys()
    for node in all_nodes:
      edges = self.adjacent_list[node]
      connections = ""

      for vertex in edges:
        connections += vertex + " "

      print(f"{ node } --> { connections }")
      
myGraph = Graph()
myGraph.add_vertex('0')
myGraph.add_vertex('1')
myGraph.add_vertex('2')
myGraph.add_vertex('3')
myGraph.add_vertex('4')
myGraph.add_vertex('5')
myGraph.add_vertex('6')
myGraph.add_edge('3', '1')
myGraph.add_edge('3', '4')
myGraph.add_edge('4', '2')
myGraph.add_edge('4', '5')
myGraph.add_edge('1', '2')
myGraph.add_edge('1', '0')
myGraph.add_edge('0', '2')
myGraph.add_edge('6', '5')

myGraph.show_connections(); 
# Answer:
#  0-->1 2 
#  1-->3 2 0 
#  2-->4 1 0 
#  3-->1 4 
#  4-->3 2 5 
#  5-->4 6 
#  6-->5